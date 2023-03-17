# N개 마구간 x1, x2, x3 ...xN의 좌표 no 중복
# C마리 말 -> 마구간
# 가장 가까운 거리가 최대값 출력
# 3<=N<=200,000 / 2<=C<=N / 0<=xi<=1,000,000,000

import sys, traceback

sys.stdin = open("./algorithm/decision_greedy_algorithm/input.txt", "rt")

def cal_maxInterval(N:int, C:int, poList:list)->int:
    res = 0
    poList.sort()
    diff_poList = []
    for i in range(1,N):
        diff_poList.append(poList[i] - poList[i-1])
    print(diff_poList)

    lt = 1
    rt = sum(diff_poList)

    while lt <= rt:
        mid = (lt+rt)//2
        tot = 0
        cnt = 1
        for i in diff_poList:
            tot +=i
            if tot >= mid:
                tot = 0
                cnt +=1
        if cnt >= C:
            res = mid
            lt = mid +1
        elif cnt < C:
            rt = mid -1

        print(f"mid : {mid}")
        print(f"cnt : {cnt}")
        print()
    return res

def cal_Count(mid:int, diff_poList:list)->int:
    cnt = 1
    tot = 0
    for i in diff_poList:
        tot +=i
        if tot >= mid:
            tot = 0
            cnt +=1
    return cnt

try:
    N,C = map(int, input().split())
    poList = list(int(input()) for _ in range(N))
    #print(cal_maxInterval(N,C,poList))
    poList.sort()
    diff_poList = []
    
    for i in range(1,N):
        diff_poList.append(poList[i] - poList[i-1])
    print(diff_poList)
    
    lt = 1
    rt = sum(diff_poList)
    while lt <= rt:
        mid = (lt+rt)//2
        if cal_Count(mid,diff_poList) >=C:
            res = mid
            lt = mid +1
        else:
            rt = mid =1
    print(mid)

except Exception as e:
    traceback.print_exc()
    print("[ERROR]",e)