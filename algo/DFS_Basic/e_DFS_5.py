# c : 차량 제한 무게, n : n마리, w : 각 바둑이 무게
import traceback, sys

sys.stdin = open("./algo/DFS_Basic/input.txt", "rt")

def DFS(w_dList:list,cnt:int):
    global sum_v
    global res
    if c == sum_v:
        res = sum_v
        sys.exit(0)
    if c < sum_v:
        return
    
    if cnt == n:
        if c > sum_v:
            if res < sum_v:
                res = sum_v
    
    else:
        w_dList[cnt][1]=1
        sum_v +=w_dList[cnt][0]
        DFS(w_dList,cnt+1)
        w_dList[cnt][1]=0
        sum_v -=w_dList[cnt][0]
        DFS(w_dList,cnt+1)
        

try:
    c,n = map(int, input().split())
    w_list = [int(input()) for _ in range(n)]
    #w_dict = {value:0 for key, value in enumerate(w_list)} # enumerate를 활용한 list -> dict 전환
    w_dList = [[i,0] for i in w_list]
    cnt = 0
    res = 0
    sum_v = 0
    DFS(w_dList,cnt)
    print(res)

except Exception as e:
    traceback.print_exc()
    print("[ERROR]",e)