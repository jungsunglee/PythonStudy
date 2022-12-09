# N(1<=N<=10,000)개 수열 -> i ~ j까지 수의 합이 M이 되는 경우의 수
# M(1<=M<=300,000,000) / A[x] <= 30,000
import traceback, sys

def sum_case(N: int,M: int,prog:list)->int:
    cnt = 0
    cnt +=prog.count(M)
    for i in range(N): # i 0 ~ 99 N 100
        for j in range(i+1,N): # range(8,8)이면 동작하지 않음 즉, 같은 수가 들어오면 동작하지 않음
            # 이중 for 문 사용 시 data가 크면 성능에 issue 발생할 수 있음
            if sum(prog[i:j+1]) == M: # 반복문안에 method 등을 사용할 경우 process 성능이 저하됨
                # j+1을 한 이유 : 리스트 슬라이싱은 j전까지의 합이다.
                cnt +=1
                break
    return cnt

# Solution : while문을 사용하는 방법만 존재 성능이 안나옴
# 반복문을 하나만 사용해야 함.
def sum_case_sol(N: int,M: int,prog:list)->int:
    cnt = 0
    tot =0
    lt = 0
    rt = 0
    while True:
        if tot < M:
            if rt < N:
                tot +=prog[rt]
                rt+=1
            else:
                break
        elif tot ==M:
            cnt +=1
            tot -=prog[lt]
            lt += 1
        else:
            tot -=prog[lt]
            lt +=1
                
    return cnt

sys.stdin = open("./algorithm/string_1st_2nd_List/input.txt", "rt")
try:
    N,M = map(int, input().split())
    prog = list(map(int, input().split()))

    if not 1<=N<=10000: # not으로 조건문 간단하게 가능 중요
        raise Exception("Out of range,1<=N<=10,000")
    elif not 1<=M<=300000000:
        raise Exception("Out of range,1<=M<=300,000,000")
    print(sum_case_sol(N,M,prog))

except Exception as e:
    traceback.print_exc()
    print("[ERROR]",e)