from collections import deque
import sys

cnt = int(input())

q = deque()

for i in range(cnt):
    datas = sys.stdin.readline().split()
    if "push_front" == datas[0]:
        q.appendleft(datas[1])
    elif "push_back" == datas[0]:
        q.append(datas[1])
    elif "pop_front" == datas[0]:
        if len(q):print(q.popleft())
        else:print(-1)
    elif "pop_back" == datas[0]:
        if len(q):print(q.pop())
        else:print(-1)
    elif "size" == datas[0]:print(len(q))
    elif "empty" == datas[0]:
        if len(q):print(0)
        else:print(1)
    elif "front" == datas[0]:
        if len(q):print(q[0])
        else:print(-1)
    elif "back" == datas[0]:
        if len(q):print(q[len(q)-1])
        else:print(-1)
