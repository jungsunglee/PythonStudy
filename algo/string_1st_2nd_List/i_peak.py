### 이거 한번 더 풀어보기
# N*N Grid / 가장자리 0으로 초기화
# 해당 숫자에서 상하좌우보다 큰 수자의 개수
import sys, traceback

sys.stdin = open("./algorithm/string_1st_2nd_List/input.txt", "rt")

def cal_peak(N: int, grid: list)->int:
    count = 0
    # Solution 참고 4방향 탐
    condI = [-1, 1, 0, 0]
    condJ = [0, 0, -1, 1]
    for i in range(1,len(grid)-1):
        for j in range(1, len(grid[i])-1):
            if all(grid[i][j] > grid[i+condI[x]][j+condJ[x]] for x in range(4)):
                # all을 사용하기 위해 condI, J list를 만들어서 적용
                count +=1
    return count

try:
    N = int(input())
    grid = [list(map(int, input().split())) for _ in range(N)]
    grid.insert(0,[0]*N)
    grid.insert(N+1,[0]*N)
    for i in range(N+2):
        grid[i].insert(0,0)
        grid[i].append(0)
    print(cal_peak(N, grid))
    
except Exception as e:
    traceback.print_exc()
    print("[ERROR]",e)