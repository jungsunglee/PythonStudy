# 1 ~ n 수열 / 역수열 원복
import sys, traceback
from collections import deque

sys.stdin = open("./algorithm/decision_greedy_algorithm/input.txt", "rt")

def recoverNum(n:int, inList:list) -> deque:
    res = deque()
    inList = inList[::-1]
    for i in inList:
        res.insert(i,n)
        n -= 1
    
    return res


try:
    n = int(input())
    inList = list(map(int,input().split()))

    print(*recoverNum(n,inList))
    #print(" ".join(str(x) for x in recoverNum(n,inList)))

except Exception as e:
    traceback.print_exc()
    print("[ERROR]",e)