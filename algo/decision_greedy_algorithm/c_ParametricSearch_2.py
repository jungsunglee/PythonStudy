# 1<=N<=1,000 / 1<=M<=N / 곡은 10,000분을 넘지 않음
# M : DVD 개수 / N : DVD에 들어가는 곡 개수
# DVD 최소 용량 크기
import sys, traceback

sys.stdin = open("./algorithm/decision_greedy_algorithm/input.txt",'rt')

def calDVDlen(N:int, M:int, songList:list) -> int:
    lt = 1
    rt = sum(songList)
    res = 0

    while lt <=rt:
        mid = (lt+rt)//2
        tot = 0
        cnt = 1
        for i in songList:
            tot += i
            if tot > mid:
                cnt+=1
                tot=i
        if cnt <= M:
            res = mid
            rt = mid-1
        elif cnt > M:
            lt = mid+1
    return res

try:
    N, M = map(int, input().split())
    songList = list(map(int,input().split()))
    print(calDVDlen(N,M,songList))

except Exception as e:
    traceback.print_exc()
    print("[ERROR]",e)