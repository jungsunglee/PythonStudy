# 1 ~ N까지 자연수 수열

import sys, traceback
from collections import deque

sys.stdin = open("./algorithm/decision_greedy_algorithm/input.txt", "rt")

def cal_increSeq(N:int, inDeque:deque) -> list:
    res = []
    ref = 0
    while True:
        if len(inDeque) == 1:
            if inDeque.pop() > ref:
                res.append("L")
            break
        lv = inDeque.popleft()
        rv = inDeque.pop()
        if ref < lv and ref < rv:
            if lv < rv:
                res.append("L")
                inDeque.append(rv)
                ref = lv
                #print(lv)
            elif lv > rv:
                res.append("R")
                inDeque.appendleft(lv)
                ref = rv
                #print(rv)
        elif ref < lv and ref > rv:
            res.append("L")
            inDeque.append(rv)
            ref = lv
            #print(lv)
        elif ref < rv and ref > lv:
            res.append("R")
            inDeque.appendleft(lv)
            ref = rv
            #print(rv)
        else:
            break
    return res

try:
    N = int(input())
#    inList = list(map(int, input().split()))
#    inDeque = deque(inList)
    inDeque = deque(map(int, input().split()))

    reList = cal_increSeq(N, inDeque)

    print(len(reList))
    print(''.join(x for x in reList))


except Exception as e:
    traceback.print_exc()
    print("[ERROR]",e)