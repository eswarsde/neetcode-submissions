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


# why is this backtracking 

# This is a textbook example of a **backtracking** algorithm. While backtracking is built on top of the Depth-First Search (DFS) mechanism, the key difference lies in how it manages the state (in this case, the `stack` variable).

# Here is exactly what makes this code backtracking rather than a standard DFS traversal.

# ### 1. The "Choose, Explore, Un-choose" Pattern

# The defining characteristic of backtracking is that it uses a single, shared mutable data structure (your `stack` list) to build a potential solution, and it explicitly **undoes** its choices when it returns from a recursive call.

# Look at this specific block of your code:

# ```python
# if open_count < n:
#     stack.append("(")                        # 1. CHOOSE: Make a choice
#     dfs_backtrack(open_count + 1, closed_count) # 2. EXPLORE: Recurse down this path
#     stack.pop()                              # 3. UN-CHOOSE: Undo the choice (Backtrack)

# ```

# When the recursive `dfs_backtrack` call finishes (either by hitting the base case or exhausting options), the code executes `stack.pop()`. This removes the `(` or `)` it just added. It "backtracks" to the previous state so that the algorithm can cleanly try the next available choice (the `if closed_count < open_count` block) without the `stack` being contaminated by the previous path's data.

# ### 2. Shared Mutable State vs. Passing State Forward

# In a "regular" DFS, especially when searching a tree or a graph, you typically pass the state forward by value, or you use immutable data structures. You usually don't need an explicit "undo" step.

# If you were to write this exact same logic as a **regular DFS** without backtracking, you would pass an immutable string down the recursive calls instead of modifying a shared list. It would look like this:

# ```python
# result = []
# def dfs(open_count, closed_count, current_string):
#     # base case 
#     if open_count == closed_count == n:
#         result.append(current_string)
#         return 
    
#     if open_count < n:
#         # Notice we just create a new string and pass it down. 
#         # No .pop() or undo step is needed when it returns.
#         dfs(open_count + 1, closed_count, current_string + "(")

#     if closed_count < open_count:
#         dfs(open_count, closed_count + 1, current_string + ")")

# dfs(0, 0, "")

# ```

# ### Summary

# * **Regular DFS:** Moves forward through a search space, often passing the accumulated state down the chain. It relies on the call stack to remember where it was.
# * **Backtracking (Your Code):** Actively modifies a single variable (`stack.append`) to step forward, and actively reverts that variable (`stack.pop`) to step backward. This is much more memory efficient than creating new strings for every single recursive call, which is why backtracking is the standard approach for combinatorial generation problems like this one.