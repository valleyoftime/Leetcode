# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSameTree(self, p: TreeNode | None, q: TreeNode | None) -> bool:
        if not p and not q:
            return True
        if not p or not q:
            return False
        
        return True if p.val == q.val and self.isSameTree(p.left, q.right) and self.isSameTree(p.right, q.left) else False

    def isSymmetric(self, root: TreeNode | None) -> bool:
        if not root:
            return True

        return True if self.isSameTree(root.left, root.right) else False