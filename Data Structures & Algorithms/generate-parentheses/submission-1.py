class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        # brute force 
        # if n = 3, => tell us there 3 open and 3 closed paranthesis
        #   # valid answers should always start with open paranthesis and end with closed paranthesis   
        #   # at any given point, the number of close paranthesis cannot be > open paranthesis count 
        #   # we always add n number of paranthesis irrespective of closed paranthesis count. example "((()))"
        # better apprach 
        # How do we model this problem 
        # we can model this as a tree/graph -> at any point, we have several choices -> based on the count of the open and close postions and n.
        # and when making choices we follow the rules that makes a valid paranthesis arrangement by following all of those rules mentioned in brute force approach - this way we actively avoid/prune bad solutions

        # backtracking Explicit state => recursion doesn't handle the stack for yoy 
        stack = []
        result = []
        def dfs_backtrack(open_count, closed_count):

            # base case 
            if open_count == closed_count == n:
                result.append("".join(stack))
                return 
            
            # business conditions 
            # choices => choose => explore => un-choose
            if open_count < n:
                stack.append("(")
                dfs_backtrack(open_count + 1, closed_count)
                stack.pop()

            if closed_count < open_count:
                stack.append(")")
                dfs_backtrack(open_count, closed_count + 1)
                stack.pop()

        dfs_backtrack(0, 0)

        return result       