# N : 왕자 수, K : 번호
import sys, traceback
from collections import deque

sys.stdin = open("./algo/data_structure_stack_queue_hash_heap/input.txt", "rt")

def sel_prince(N:int, K:int) -> int:
    res = 0
    queue = deque(i for i in range(1,N+1))
    while len(queue) != 1:
        queue.rotate(-(K-1))
        queue.popleft()
        if len(queue) ==1:
            res = queue[0]


    return res

def sel_prince_sol(N:int, K:int) -> int:
    res = 0
    cnt = 1
    queue = deque(i for i in range(1,N+1))
    while queue:
        if cnt != K:
            cnt += 1
            queue.append(queue.popleft())
        elif cnt ==K:
            cnt = 1
            queue.popleft()

        if len(queue) == 1:
            res = queue.popleft()
    return res

try:
    N, K = map(int,input().split())
    print(sel_prince_sol(N,K))

except Exception as e:
    traceback.print_exc()
    print("[ERROR]",e)