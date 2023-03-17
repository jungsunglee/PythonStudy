# N명 승객 -> 탈출 -> 구명보트 2명 이하 탑승 / 무게 Mkg 제한
# N면 승객 몸무게 -> 모두 탈출 ->구명보트 최소 개수
# 5<=N<=1000 / 70<=M<=250 / 50<=몸무게<=150
import sys, traceback
from collections import deque

sys.stdin = open("./algorithm/decision_greedy_algorithm/input.txt", "rt")

def calMinBoat(N:int, M:int, weightList:list)->int:
    cnt = 1
    tot = 0
    weightList.sort(reverse=True)
    while len(weightList) !=0:
        first = weightList.pop(0)
        tot += first
        for _ in range(len(weightList)):
            last = weightList.pop()
            tot += last
            if tot > M:
                cnt += 1
                weightList.append(last)
                tot = 0
                break
            elif tot == M:
                cnt +=1
                tot = 0
                break
    return cnt

def calMinBoat_deque(N:int, M:int, weightList:list)->int:
    cnt = 0
    weightList.sort(reverse=True)
    deque_WL = deque(weightList)
    while deque_WL:
        if len(deque_WL)==1:
            cnt+=1
            break
        if deque_WL[0] + deque_WL[-1] > M:
            deque_WL.popleft()
            cnt +=1
        else:
            deque_WL.pop()
            deque_WL.popleft()
            cnt+=1

    return cnt

try:
    N,M = map(int, input().split())
    weightList = list(map(int, input().split()))
    print(calMinBoat_deque(N,M,weightList))

except Exception as e:
    traceback.print_exc()
    print("[ERROR]",e)