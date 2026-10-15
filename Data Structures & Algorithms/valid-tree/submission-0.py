class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        adj = {i: [] for i in range(n)}
        for a, b in edges:
            adj[a].append(b)
            adj[b].append(a)
        
        visited = set()

        def dfs(node, parent):
            visited.add(node)

            for nei in adj[node]:
                if nei == parent:
                    continue
                
                if nei in visited:
                    return False
                
                if not dfs(nei, node):
                    return False
            return True

        return dfs(0, -1) and len(visited) == n

        # T: O(V + E)
        # S: O(V + E)