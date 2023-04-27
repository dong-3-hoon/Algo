from collections import deque

dq = deque([1, 2, 3, 4, 5])

dq.append(1)
print(dq)
dq.popleft()
print(dq)
