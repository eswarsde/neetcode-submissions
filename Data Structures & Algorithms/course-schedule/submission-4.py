from collections import deque, defaultdict

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        # Step 0: Convert Edge List to Adjacency List
        # Step 1. Calculate the indegree of each node
        indegree = [0] * numCourses
        prereq_to_courses_adj_list = defaultdict(list)
        for course, prereq in prerequisites:
            prereq_to_courses_adj_list[prereq].append(course) # a given course is preq for what courses
            indegree[course]+=1


        # 2. Initialize the Queue with all "0 prerequisite" nodes
        queue = deque([course for course, prereq_count in enumerate(indegree) if prereq_count == 0])

        # 3. The Modified BFS Loop
        completed = 0
        while queue:
            curr = queue.popleft()
            completed +=1

            # "Complete" the current course by freeing up the courses that depend on it
            for next_course in prereq_to_courses_adj_list.get(curr, []):
                indegree[next_course] -=1

                # If the neighbor has no more prerequisites, it's ready!
                if indegree[next_course] == 0:
                    queue.append(next_course)

        # 4. Cycle Detection Check and return 

        return completed == numCourses







        