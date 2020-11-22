# ============================================
# Leetcode 26. 删除排序数组中的重复项
# 审题: 1. 原地删除，空间复杂度为O(1); 2.数组已为排序过的数组; 3)只需返回新数组的长度。
# seen before
# 解体思路: 快慢指针
# time complexity: O(n)
# ============================================


class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        slow = 0
        fast = 1
        while (fast <= len(nums) - 1):
            if nums[slow] == nums[fast]:
                fast += 1
            else:
                slow += 1
                nums[slow] = nums[fast]
                fast += 1
        return slow+1

