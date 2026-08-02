from collections import deque, defaultdict

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        # We can model this question as a graph 
        # Each course is a node, and each prerequisite is a directed edge.
        # one can finsih all courses if there is no cycle in a directed graph

        # Algorithm - Khan's Algorithm (Modified BFS)

        # Step 1:
        # if input given is edge list convert it to adj_list and also calculate indegree for each course

        # [a, b]  must take course b first if you want to take course a.
        # [b -> a] -> a is 1 indegree, course a has one preq
        course_indegree = [0] * numCourses
        pre_req_to_courses_adj_list = defaultdict(list)
        for course, pre_req in prerequisites:
            pre_req_to_courses_adj_list[pre_req].append(course)
            course_indegree[course] += 1

        
        # Step 2. Initialize the Queue with all "0 prerequisite" nodes
        queue = deque([course for course, pre_req_count in enumerate(course_indegree) if pre_req_count == 0])
        
        # Step 3: Process the queue unitl it becomes empty
        finished_count = 0
        while queue:
            curr_course = queue.popleft()
            finished_count += 1

            # now that the curr_course is completed, reduce indegree for all the courses to which curr_course was a pre_req     
            for course in pre_req_to_courses_adj_list[curr_course]:
                course_indegree[course] -=1

                # If the neighbor has no more prerequisites, it's ready!
                if course_indegree[course] == 0:
                    queue.append(course) 

#         # 4. Cycle Detection Check and return 
#         # If we were able to take all courses, return True.
#         # Otherwise (if there is a cycle), return False.
        return finished_count == numCourses



# Time complexity: O(V+E)
# Space complexity: O(V+E)

# V is the number of courses and 
# E is the number of prerequisites.



        