import sys, traceback

sys.stdin = open("./algo/DFS_Basic/input.txt", "rt")

def DFS(p:int):
    global cnt
    if p == m:
        print(" ".join(str(i) for i in res))
        cnt+=1
    else:
        for i in range(1, n+1):
            res[p] = i
            DFS(p+1)

try:
    n,m = map(int, input().split())
    L = [int(i+1) for i in range(n)]
    res = [0]*m
    cnt = 0
    DFS(0)
    print(cnt)

except Exception() as e:
    traceback.print_exc()
    print("[ERROR]",e)