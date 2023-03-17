# K(1<=K<=10,000) : 랜선 개수, N(1<=N<=1,000,000) : 필요한 랜선 개수
# K <= N
# N개를 만들 수 있는 랜선의 최대 길이
import sys, traceback

sys.stdin = open("./algorithm/decision_greedy_algorithm/input.txt", "rt")

def calMaxCable(K:int, N:int, cableList:list) -> int:
    lt = 1
    rt = max(cableList)
    result = 0   
    while lt<=rt:
        tot = 0
        mid = (lt+rt)//2
        for i in cableList:
            tot +=i//mid
        if tot >= N:
            if result < mid:
                result = mid
            lt = mid +1
        elif tot < N:
            rt = mid -1
    return result

try:
    K, N = map(int, input().split())
    cableList = list(int(input()) for _ in range(K))
    print(calMaxCable(K, N, cableList))
    
except Exception as e:
    traceback.print_exc()
    print("[ERROR]",e)