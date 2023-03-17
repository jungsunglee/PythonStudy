import traceback, sys, time

sys.stdin = open("./algo/DFS_Basic/input.txt", "rt")

def DFS(P:int, tot:int):
    global res

    if P == N:
        if res < tot < C:
            res = tot
    else:
        DFS(P+1,tot+dog_list[P])
        DFS(P+1,tot)
try:
    start_time = time.time()
    C,N = map(int, input().split())
    dog_list = [int(input()) for _ in range(N)]
    dog_list = sorted(dog_list, reverse=True)
    res = 0
    if C > sum(dog_list):
        print(sum(dog_list))
    else:
        DFS(0,0)
        print(res)
    #print(f"Operating Time : {time.time()-start_time}")

except Exception as e:
    traceback.print_exc()
    print("[ERROR]", e)