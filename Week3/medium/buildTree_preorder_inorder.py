# ============================================
# 105. Construct Binary Tree from Preorder and Inorder Traversal
# 审题: You may assume that duplicates do not exist in the tree.
# not seen before, not solved alone, idea following the solutions proposed in leetcode
# 解体思路: 1.递归；2.迭代
# time complexity: 1.recursive: O(n), n=Tree.size
# ============================================



# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# TODO, 不是最优解法，还需改进内存与速度
class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        # recursion terminator
        if (len(preorder) <= 0) or (len(inorder) <= 0):
            return None

        # process current level
        root = TreeNode()
        root.val = preorder[0]
        in_pointer = inorder.index(root.val)

        # drill down
        # in_pointer also means the number of left nodes here
        root.left = self.buildTree(preorder[1:in_pointer + 1], inorder[0:in_pointer])
        root.right = self.buildTree(preorder[in_pointer + 1:], inorder[in_pointer + 1:])
        # reverse
        # merge
        return root