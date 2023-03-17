### 이거 한번 더 풀어보기
import sys, traceback

sys.stdin = open("./algorithm/string_1st_2nd_List/input.txt", "rt")

def checkSudoku(grid9:list) -> str:
    
    critValue = 45
    condI = [0,1,2]
    condJ = [0,1,2]
    result ='YES'
    
    for i in range(9):
        sumRow = sum(grid9[i])
        dupResult_Row = check_dup(grid9[i])
        if sumRow != 45 or dupResult_Row == False:
            result = 'NO'
            return result 
        sumColum = sum(grid9[i][j] for j in range(9))
        dupResult_Col = check_dup(grid9[i][j] for j in range(9))
        if sumColum != 45 or dupResult_Col == False:
            result = 'NO'
            return result
        if i == 0 or i == 3 or i == 6:
            for j in range(0,7,3):
                grid3Sum = 0
                grid3List = []
                for a in condI:
                    for b in condJ:
                        grid3Sum+=grid9[i+a][j+b]
                        grid3List.append(grid9[i+a][j+b])
                dupResult_Grid3 = check_dup(grid3List)
                if grid3Sum != 45 or dupResult_Grid3 == False:
                    result = 'NO'
                    return result
    return result

def check_dup(inlist:list) -> bool:
    chSet = set(inlist)
    outList = list(chSet)
    numVal = len(outList)
    if numVal != 9:
        return False
    else:
        return True

# Solution
def checkSudoku_Sol(grid9:list) -> str:
    for i in range(9):
        ch_Row = [0]*10
        ch_Col = [0]*10
        for j in range(9):
            ch_Row[grid9[i][j]] = 1
            ch_Col[grid9[j][i]] = 1
        
        if sum(ch_Col) or sum(ch_Row) != 9:
            return "NO"

    for i in range(3):
        for j in range(3):
            ch_grid3 = [0]*10
            for a in range(3):
                for b in range(3):
                    ch_grid3[grid9[3*i+a][3*j+b]] = 1
            if sum(ch_grid3) != 9:
                return "NO"
    return "YES"


try:
    grid9 = [list(map(int, input().split())) for _ in range(9)]
    print(checkSudoku_Sol(grid9))

except Exception as e:
    traceback.print_exc()
    print("[ERROR]",e)