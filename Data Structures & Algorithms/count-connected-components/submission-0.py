class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj = {i: [] for i in range(n)}
        for a, b in edges:
            adj[a].append(b)
            adj[b].append(a)

        visited = set()
        count = 0

        def dfs(node):
            # base case
            if node in visited:
                return
            
            visited.add(node)
            
            for nei in adj[node]:
                dfs(nei)


        for node in range(n):
            if node not in visited:
                dfs(node)
                count += 1

        return count
    
    # T: O(V + E)
    # S: O(V + E)
        
        