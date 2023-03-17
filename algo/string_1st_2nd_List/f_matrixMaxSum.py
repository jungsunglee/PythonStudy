# 자연수 N(1<=N<=50) -> NxN matirx
# 각 행, 열, 대각선의 합중 가장 큰 합 출력
import sys, traceback

sys.stdin = open("./algorithm/string_1st_2nd_List/input.txt", "rt")

def cal_maxSum(N:int, matrix:list) -> int:
    totC1=0
    totC2=0
    re = []
    for i in range(N):
        tot1 = tot2 = 0
        for j in range(N):
            tot +=matrix[i][j]
            tot +=matrix[j][i]
        re.append(tot1)
        re.append(tot2)
    for i in range(N):
        a +=matrix[i][i]
        b +=matrix[i][N-i-1]
    re.append(totC1)
    re.append(totC2)    
    return max(re)

try:
    N = int(input())
    matrix = [list(map(int, input().split())) for _ in range(N)] # 이중 list 입력 받아 만드는 법
    print(cal_maxSum(N,matrix))

except Exception as e:
    traceback.print_exc()
    print("[ERROR]",e)