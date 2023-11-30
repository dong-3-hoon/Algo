from collections import deque
import sys
queue = deque

T = sys.stdin.readline

for i in range(T):
    lst = list(map(str, input().split()))
    if lst[0] == 'push':
        queue.put(int(lst[1]))
    elif lst[0] == 'pop':
        queue.popleft()
    elif lst[0] == 'front':
        if len(queue) == 0:
            print(-1)
        else:
            print(queue[0])
    elif lst[0] == 'back':
        if len(queue) == 0:
            print(-1)
        else:
            print(queue[len(queue)])
    elif lst[0] == 'size':
        print(len(queue))
    elif lst[0] == 'empty':
        if len(queue) == 0:
            print(1)
        else:
            print(0)