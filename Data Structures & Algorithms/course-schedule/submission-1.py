from collections import deque, defaultdict

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        # Step 0: Convert Edge List to Adjacency List
        # Step 1. Calculate the indegree of each node
        indegree = [0] * numCourses
        adj_list = defaultdict(list)
        for u, v in prerequisites:
            adj_list[v].append(u)
            indegree[u]+=1


        # 2. Initialize the Queue with all "0 prerequisite" nodes
        queue = deque([i for i, val in enumerate(indegree) if val == 0])

        # 3. The Modified BFS Loop
        completed = 0
        while queue:
            curr = queue.popleft()
            completed +=1

            # "Complete" the current node by freeing up its neighbors
            for neighbour in adj_list.get(curr, []):
                indegree[neighbour] -=1

                # If the neighbor has no more prerequisites, it's ready!
                if indegree[neighbour] == 0:
                    queue.append(neighbour)

        # 4. Cycle Detection Check and return 

        return completed == numCourses







        