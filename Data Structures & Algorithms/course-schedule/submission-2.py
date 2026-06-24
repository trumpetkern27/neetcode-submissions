class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = {i: [] for i in range(numCourses)}
        for c, p in prerequisites:
            graph[c].append(p)
        
        
        visiting = set()
        def dfs(n):
            if n in visiting:
                return False
            if graph[n] == []:
                return True
            visiting.add(n)
            for e in graph[n]:
                if not dfs(e):
                    return False
            visiting.remove(n)
            graph[n] = []
            return True

        for c in range(numCourses):
            if not dfs(c):
                return False
        return True
     