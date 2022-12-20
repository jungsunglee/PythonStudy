### 이거 한번 더 풀어보기
# N*N(3<=N<=20) N : odd number 격자 -> 2 0 3 입력시 2번째 행을 외쪽으로 3만큼 회전 0 : 왼쪽 / 1 :오른쪽
# M(1<=M<=10)개 회전 명령 실행 후 모래시계 모양 영역의 sum
import sys, traceback

sys.stdin = open("./algorithm/string_1st_2nd_List/input.txt", "rt")
def rotate(M: int, N: int, matrix: list, rotateList: list )-> list:
    for i in range(M):
        row = rotateList[i][0]-1
        dir = rotateList[i][1]
        count = rotateList[i][2]
        if dir == 0:
            for _ in range(count):
                matrix[row].append(matrix[row].pop(0))
        else:
            for _ in range(count):
                matrix[row].insert(0,matrix[row].pop())
        
    return matrix

def cal_tot(N:int, matrix: list)->list:
    tot = 0
    cV = N//2
    lV = 0
    rV = N
    for i in range(N):
        for j in range(lV, rV):
            tot += matrix[i][j]
        if i < cV:
            lV +=1
            rV -=1
        else:
            lV -=1
            rV +=1
    return tot

try:
    N = int(input())
    matrix = [list(map(int, input().split())) for _ in range(N)]
    M = int(input())
    rotateList = [list(map(int, input().split())) for _ in range(M)]
    rotated_list = rotate(M, N, matrix, rotateList)
    print(cal_tot(N, rotated_list))

except Exception as e:
    traceback.print_exc()
    print("[ERROR]",e)
