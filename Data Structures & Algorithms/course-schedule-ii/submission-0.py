class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # adjacency list
        adj = {i: [] for i in range(numCourses)}

        for course, pre in prerequisites:
            adj[course].append(pre)

        visiting = set()
        res = []

        def dfs(course):
            # cycle detected
            if course in visiting:
                return False
            
            # already processed and added to result
            if adj[course] is None:
                return True
            
            visiting.add(course)

            for pre in adj[course]:
                if not dfs(pre):
                    return False

            visiting.remove(course)
            adj[course] = None
            res.append(course) 
            return True

        
        for i in range(numCourses):
            if not dfs(i):
                return []
        
        return res

        # T: O(V + E)
        # S: O(V + E)
        
