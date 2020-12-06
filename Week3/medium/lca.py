# ============================================
# 236. Lowest Common Ancestor of a Binary Tree
# 审题:
# not seen before, not solved alone, idea following the solutions proposed in leetcode
# 解体思路: 1.递归；2.迭代
# time complexity: 1.recursive: O(n), n=Tree.size
# ============================================

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# TODO, this solution is not efficient
class Solution1(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        if (root == None) or (root == p) or (root == q):
            return root
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)

        if (left) and (right):
            return root
        else:
            if left:
                return left
            elif right:
                return right


class Solution2(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        if root in (None, p, q):
            return root
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)

        if all((left, right)):
            return root
        else:
            if left:
                return left
            elif right:
                return right
