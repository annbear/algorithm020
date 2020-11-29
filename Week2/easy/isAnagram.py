# ============================================
# Leetco 242. 有效的字母异位词
# 审题: 1. 进阶的情况: 如果输入字符串包含 unicode 字符怎么办？你能否调整你的解法来应对这种情况
# not seen before
# 解体思路: 字典形式储存词频
# time complexity: O(2n)≈O(n)
# ============================================


# TODO Solution1
#执行用时：48 ms, 在所有 Python 提交中击败了51.42%的用户
#内存消耗：14.9 MB, 在所有 Python 提交中击败了11.08%的用户
class Solution1(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        # record the frequency/count of letters in s by key-value data structure
        dict_ct = {}
        if len(s) != len(t):
            return False
        for i in range(len(s)):
            if s[i] not in dict_ct:
                dict_ct[s[i]] = 0
            dict_ct[s[i]] += 1
        for i in range(len(t)):
            if t[i] in dict_ct:
                dict_ct[t[i]] -= 1
            else:
                return False

            if dict_ct[t[i]] == 0:
                del dict_ct[t[i]]

        return (not dict_ct)


# TODO 内存还是没有上来
class Solution2(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(s):
            return False
        if sorted(s) == sorted(t):
            return True
        else:
            return False