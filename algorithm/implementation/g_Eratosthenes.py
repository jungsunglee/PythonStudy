# 자연수 N 입력 1 ~ N까지의 소수 출력(2 <= N <= 200,000)
# 제한 시간 1초
import sys
import traceback
from time import time as t

# Solution
def sol(N:int)-> int:
    numList = [0] * (N+1)
    cnt = 0
    for i in range(2,N+1):
        if numList[i] == 0:
            cnt += 1
            for x in range(i, N+1, i):
                numList[x] = 1
    return cnt

sys.stdin = open("./algorithm/implementation/input.txt", "rt")
start = t()
try:
    N = int(input())
       
    numList = list(range(2,N+1))
    numTable = [1] * (N-1)
    #numList = list(a for a in range(2,N+1))
    for a in numList:
        if a * 2 <= N:
            for b in range(2, N//a+1):
                numTable[a*b-2]=0
        else:
            break
    print(numTable.count(1))      

except Exception as e:
    traceback.print_exc()
    print("[ERROR] ", e)
finally:
    end = t()
    print(f"{end - start:.2f}sec") # :.2f는 소숫점 둘째자리 까지 출력

