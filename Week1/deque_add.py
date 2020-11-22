"""用 add first 或 add last 这套新的 API 改写 Deque 的代码"""
## 不太明白题意

from collections import deque

class Deque_bis(object):

    # nums built from deque
    def add_last(self, nums, obj):
        return nums.append(obj)


    def add_first(self, nums, obj):
        return nums.appendleft(obj)



