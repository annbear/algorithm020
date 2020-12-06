# ============================================
# Leetco 347. 前 K 个高频元素
# 审题: 1. 对一个node的定义，判断一个node，直接可以if node，无需node.val, 不然会有'NoneType has no attribute of val'。
# not seen before
# 解体思路: 1.哈希表储存，再进行排序；2.heapq(堆) (O(NlogK)); 3.sort (O(NlogN))
# time complexity: 1.O(NlogN);
# ============================================

