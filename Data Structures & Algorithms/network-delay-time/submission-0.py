class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj = {i:[] for i in range(1, n + 1)}

        for u, v, t in times:
            adj[u].append((v, t))

        h = [(0, k)] #heap
        visited = set()
        max_time = 0
        
        while h:
            dist, node = heapq.heappop(h)

            if node in visited: # we've already finalized the short dist to this node
                continue
            visited.add(node)

            max_time = dist

            # bfs - explore neighbors
            for nei, weight in adj[node]:
                if nei not in visited:
                    heapq.heappush(h, (dist + weight, nei))
        
        return max_time if len(visited) == n else -1

    # T: O((E + V) log V)
    # S: O(E + V)