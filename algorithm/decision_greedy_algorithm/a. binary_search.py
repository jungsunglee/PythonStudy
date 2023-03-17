# N(3<=N<=1,000,000)개 수 -> 오름차순 -> M이 몇 번째 수 인지 구함
# Binary Search 사용
import sys, traceback

sys.stdin = open("./algorithm/decision_greedy_algorithm/input.txt", "rt")
def findLocation(N:int, M:int, nList:list)->int:
    lt=0
    rt=N-1
    nList.sort()
    while lt<=rt:
        mid = (lt+rt)//2
        if nList[mid] == M:
            return mid+1
        elif nList[mid] > M:
            rt = mid -1
        elif nList[mid] < M:
            lt = mid+1

try:
    N,M = map(int, input().split())
    nList = list(map(int,input().split()))
    print(findLocation(N,M,nList))
except Exception as e:
    traceback.print_exc()
    print("[ERROR]",e)