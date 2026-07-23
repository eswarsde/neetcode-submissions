# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:


        def dfs(node, curr_sum): # Q1: params = top-down state (running sum)
            
            # Base Case
            if not node: # Q5: Base case
                return False
            
            curr_sum = curr_sum + node.val # Q4: act BEFORE recursing (top-down)
        
            # Problem specific condition
            # Q0/Q4: the "realizing" node is a leaf
            if not node.left and not node.right and curr_sum == targetSum:
                return True

            # recurse 
            return dfs(node.left, curr_sum) or dfs(node.right, curr_sum)


        return dfs(root, 0)

 # ===============================================
# 🌳 DFS TREE THINKING TEMPLATE (v2)
# ===============================================

# You are a node. Before coding, answer:

# 0️⃣ WHAT IS THE QUESTION AT MY(Node) LEVEL?
#    Rephrase the problem as a question ONE node must answer.
#    Often this is NOT the original problem -- it's a helper
#    question whose answers combine to solve the original.
#    (e.g., problem asks "diameter", node answers "my height")
#    from a node perspective - just need to if either of the subtress + node.val add upto traget

# 1️⃣ TOP-DOWN: Do I need info from ancestors?
#    - Running state along the root→me path?
#      (current sum, max seen so far on path, depth, bounds...)
#    → These become PARAMETERS of dfs.
#    -> sum up until that point from root

# 2️⃣ BOTTOM-UP: What must dfs(child) return so that
#    I can answer MY question?
#    - One value? Multiple? (tuple returns are fine)
#    → This defines the RETURN TYPE of dfs.
#    -> Nothing

# 3️⃣ THE SPLIT CHECK:
#    Is "what I return to my parent" == "the final answer"?
#    - Same → answer = dfs(root). Done.
#    - Different → dfs returns the EXTENDABLE/USABLE piece,
#      and the real answer is recorded in a global tracker
#      (nonlocal / self.ans) at whatever node it's realized.
#    # true or False - subtree reaches target or not

# 4️⃣ COMBINE: At my node, using (params + child returns):
#    - What candidate answer do I record (if split)?
#    - What value do I return upward?
#    - Do I return BEFORE or AFTER visiting children?
#      (preorder decision vs postorder aggregation)

# 5️⃣ BASE CASE: What does None (or a leaf) return so the
#    combine step at its parent works with zero extra ifs?
#    (Pick the identity value: 0, -inf, True, empty...)
#   -> if last node = adds upto target, then True 
#   ->

# 6️⃣ INITIAL CALL: What state does root receive?
#    What do I do with dfs(root)'s return?
#   root, root.val
        