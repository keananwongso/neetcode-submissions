class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        indegree = [0] * numCourses
        adj = {i: [] for i in range(numCourses)}
        for course, pre in prerequisites:
            adj[pre].append(course)
            indegree[course] += 1
        
        res = []
        
        q = collections.deque()
        for course in range(numCourses):
            if indegree[course] == 0:
                q.append(course)
        
        # bfs
        while q:
            node = q.popleft()

            # process node
            res.append(node)

            for neighbor in adj[node]:
                indegree[neighbor] -= 1

                if indegree[neighbor] == 0:
                    q.append(neighbor)

        # there's a cycle
        if len(res) != numCourses:
            return []

        return res