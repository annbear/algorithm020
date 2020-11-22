"""用 add first 或 add last 这套新的 API 改写 Deque 的代码"""
## 不太明白题意

from collections import deque

# initiate a deque of python
test_deq = deque([1,2,3,4,5])
# 相当于java里的add_last
test_deq.append(6)
# 相当于java里的add_first
test_deq.appendleft(0)

print(test_deq)

