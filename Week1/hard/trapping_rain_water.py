# ============================================
# Leetcode 283. 移动零
# 审题: 1.non-negative integers
# seen similar one before: nextGreaterNumber, largest rectangle?
# 解体思路: 有序stack
# time complexity: O(n)
# ============================================


class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        stack = []
        # record block value
        memo = 0
        # record total trapped rainy water
        total = 0
        for i, ele in enumerate(height[::-1]):
            while (len(stack) != 0) and (stack[-1][1] < ele):
                memo += stack.pop()[1]
            # current ele as left bound, s.top() as right bound
            if len(stack) != 0:
                volume = ele * (stack[-1][0] - i - 1) - memo
                if volume > 0:
                    total += volume
                    # stack.pop()
            stack.append((i, ele))
            memo = 0
        return total







