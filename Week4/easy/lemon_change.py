# ============================================
# 860. Lemonade Change
# 审题: 1. 一开始你手头没有任何零钱; 2. 只有5, 10, 20三种类型。
# not seen before, not solved alone, idea following the solutions proposed in leetcode
# 解体思路: 1.枚举所有可能的找零方式; 2.找零时贪心思想。
# time complexity: 1.O(n)
# ============================================


# TODO, 内存消耗太大
class Solution(object):
    def lemonadeChange(self, bills):
        """
        :type bills: List[int]
        :rtype: bool
        """
        cash_5 = 0
        cash_10 = 0
        ct = 0
        for ele in bills:
            if ele == 5:
                cash_5 += 1
            elif ele == 10:
                if cash_5 < 1:
                    return False
                cash_10 += 1
                cash_5 -= 1
            # ele == 20
            else:
                if (cash_10 > 0)  and (cash_5 > 0):
                    cash_10 -= 1
                    cash_5 -= 1
                elif (cash_5 >= 3):
                    cash_5 -= 3
                else:
                    return False
        return True


