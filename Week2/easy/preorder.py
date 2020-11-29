# ============================================
# Leetco 242. 有效的字母异位词
# 审题: 1. 对一个node的定义，判断一个node，直接可以if node，无需node.val, 不然会有'NoneType has no attribute of val'。
# not seen before
# 解体思路: 1.递归；2.stack 迭代
# time complexity: 1.recursive: O(n), n=Tree.size
# ============================================

"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""


class Solution(object):

    def preorder(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """
        vec = []
        if not root:
            return vec

        def preorder_helper(node):
            vec.append(node.val)
            if node.children:
                for child in node.children:
                    preorder_helper(child)
            return vec
        return preorder_helper(root)