# ============================================
# 455. Assign Cookies
# 审题: 1.每个孩子最多只能给一块饼干。2.你的目标是尽可能满足越多数量的孩子，并输出这个最大数值。
# not seen before, not solved alone, idea following the solutions proposed in leetcode
# 解体思路: 1.贪心思想。
# time complexity: 1.O(nlongn) + O(n) ≈ O(nlogn)
# ============================================


class Solution(object):
    def findContentChildren(self, g, s):
        """
        :type g: List[int]
        :type s: List[int]
        :rtype: int
        """
        if (len(g) == 0) or (len(s) == 0):
            return 0
        g.sort(reverse=False)
        s.sort(reverse=False)
        child = 0
        bisc = 0
        while (bisc <= len(s)-1) and (child <= len(g)-1):
            if (s[bisc] >= g[child]):
                child += 1
            bisc += 1
        return child
