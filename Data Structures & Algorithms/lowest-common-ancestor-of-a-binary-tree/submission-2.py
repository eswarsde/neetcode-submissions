# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        

        # The lowest common ancestor (LCA) is the deepest node that has both p and q as descendants.

        # This is a Binary Tree as give above with left and right nodes 

        # going DFS pipe mode

        # 0️⃣ WHAT IS THE QUESTION AT MY(Node) LEVEL?
        #    Rephrase the problem as a question ONE node must answer.
        #    Often this is NOT the original problem -- it's a helper
        #    question whose answers combine to solve the original.

        # You are a node: you are asking, hey do you have p and q down there
        # if each child returns I found one of the two, then you are good, you are that ancestor spliting
        # if both are found under same, then you just pass the finding further up


        # 1️⃣ TOP-DOWN: Do I need info from ancestors? (state)
        #    - Running state along the root→me path?
        #      (current sum, max seen so far on path, depth, bounds...)
        #    → These become PARAMETERS of dfs
        #   - Nothing

        
        # 2️⃣ BOTTOM-UP: What must dfs(child) return so that
        #    I can answer MY question?
        #    - One value? Multiple? (tuple returns are fine)
        #    → This defines the RETURN TYPE of dfs
        #  
        #     found one or both or None and which ones ??

        def dfs(node):
            # BASE Case
            if not node:
                return None
            if node == p or node == q:
                return node

            left_child = dfs(node.left)
            right_child = dfs(node.right)

            # If both sides found something, this node is the LCA
            if left_child and right_child:
                return node

             # Otherwise, pass up whichever side found a match
            return left_child if left_child else right_child


        return dfs(root)
