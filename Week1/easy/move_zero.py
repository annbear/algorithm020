# ============================================
# Leetcode 283. 移动零
# 审题: 1.必须在原数组上操作
# seen before
# 解体思路: 快慢指针
# time complexity: O(n)
# ============================================

class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        slow = 0
        fast = 1
        while (fast <= len(nums) - 1):
            if nums[slow] != 0:
                slow += 1
                fast += 1
            else:
                if nums[fast] != 0:
                    nums[slow], nums[fast] = nums[fast], nums[slow]
                    slow += 1
                    fast += 1
                else:
                    fast += 1
        return nums