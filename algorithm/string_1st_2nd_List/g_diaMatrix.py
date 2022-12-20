### 이거 한번 더 풀어보기
# N*N(3<=N<=20)
import sys, traceback

sys.stdin = open("./algorithm/string_1st_2nd_List/input.txt", "rt")

def cal_diaSum(N:int, matrix:list)->list:
    cValue = lValue = RValue = N//2
    tot = 0
    for i in range(N):
        for j in range(lValue, RValue+1):
            tot +=matrix[i][j]
        if i < cValue:
            lValue -=1
            RValue +=1
        else:
            lValue +=1
            RValue -=1
    return tot

try:
    N = int(input())
    matrix = [list(map(int, input().split())) for _ in range(N)]
    print(cal_diaSum(N,matrix))

except Exception as e:
    traceback.print_exc()
    print("[ERROR]", e)