# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:

        #=======================
        # You are a node. Someone asks:
        # "What is the answer for the subtree rooted at you?"
        # max(leftTree, rightTree) + 1

        # 1) What do I need from parent / ancestors?
        #    -> No

        # 2) What do I need from children?
        #    -> what must dfs(child) return?
        #    -> heigh of child subtree

        # 3) At current node:
        #    -> what do I compute?
        #    -> what do I return upward?
        # max(leftTree, rightTree) + 1 ??

        # 4) Base case:
        #    if node is None: return _____

        # 5) Initial call:
        #    what state does root start with?
        
        if root is None:
            return 0

        left = self.maxDepth(root.left)
        right = self.maxDepth(root.right)

        return max(left, right) + 1



   