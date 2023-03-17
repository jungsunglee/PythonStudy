import sys, traceback
from collections import deque

sys.stdin = open("./algo/data_structure_stack_queue_hash_heap/input.txt", "rt")

def cal_sequence(N:int, M:int, queue:deque) -> int:
    res = 0
    ch = queue[M]
    seq = 0
    while True:
        cnt = 0
        max = 0
        len_q = len(queue)
        for _ in range(len_q):
            cur = queue.popleft()
            cnt +=1
            if max < cur:
                max = cur
            if cnt == len_q:
                seq +=1
            else:
                queue.append(cur)
        if ch == max:
            res = seq
            break

    return res

def cal_sequence_sol(N:int, M:int, queue:deque) -> int:
    res = 0
    while True:
        cur = queue.popleft()
        if any(cur[1] < x[1] for x in queue):
            queue.append(cur)
        else:
            res +=1
            if cur[0] == M:
                return res

try:
    N, M = map(int,input().split())
    queue =deque([(num,val) for num, val in enumerate(list(map(int,input().split())))])
    print(cal_sequence_sol(N,M,queue))

except Exception as e:
    traceback.print_exc()
    print("[ERROR]",e)