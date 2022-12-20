# 7x7 grid 1~9까지 수
# 가로세로 5자리 회문 수 -> 개수

import sys, traceback

sys.stdin = open("./algorithm/string_1st_2nd_List/input.txt", "rt")

def chCirNumCount(grid7: list) -> int:
    count = 0
    for i in range(7):
        for a in range(3):
            row = []
            col = []
            for j in range(a,a+5):
                row.append(grid7[i][j])
                col.append(grid7[j][i])
            if row == row[::-1]:
                count += 1
            if col == col[::-1]:
                count += 1
    return count

try:
    grid7 = [list(map(int, input().split())) for _ in range(7)]
    print(chCirNumCount(grid7))

except Exception as e:
    traceback.print_exc()
    print("[ERROR]",e)