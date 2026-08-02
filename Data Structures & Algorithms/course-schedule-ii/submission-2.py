from collections import deque, defaultdict
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # Khan's topological sorting
        # adj_list
        # in-degree + BFS


        # Step 0 & 1: Build Adjacency List and Calculate Indegrees
        course_indegree = [0] * numCourses
        pre_req_to_courses_adj_list = defaultdict(list)

        for course, prereq in prerequisites:
            pre_req_to_courses_adj_list[prereq].append(course)
            course_indegree[course]+=1

        # 2. Initialize the Queue with courses that have 0 prerequisites
        queue = deque([course for course, prereq_count in enumerate(course_indegree) if prereq_count == 0])


        
        # 3. The Modified BFS Loop
        topological_order_completed_courses = []

        while queue:
            curr_course = queue.popleft()
            topological_order_completed_courses.append(curr_course)

            for next_course in pre_req_to_courses_adj_list.get(curr_course, []):
                course_indegree[next_course] -= 1

                if course_indegree[next_course] == 0:
                    queue.append(next_course)




        # 4. Cycle Detection Check and return 
        # If we were able to take all courses, return the valid order.
        # Otherwise (if there is a cycle), return an empty array.
        if numCourses == len(topological_order_completed_courses):
            return topological_order_completed_courses
        return []

        