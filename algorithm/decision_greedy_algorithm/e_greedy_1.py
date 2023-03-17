# n 회의의 수(1<=n<=100,000)
# 최대 회의의 수
# 각 회의의 시작시간 / 끝나는 시간 -> 겹치지 않게 
import sys, traceback

sys.stdin = open("./algorithm/decision_greedy_algorithm/input.txt", "rt")

def calTimes(n:int,StartEndlist:list) -> int:
    sor_StartEndList= sorted(StartEndList, key=lambda x:x[1]) #lamda를 활용한 뒷자리 정렬
    #sor_StartEndList= sorted(StartEndList, key=lambda x: (x[1], x[0])) #lamda를 활용한 뒷자리 정렬
    cnt = 1
    st=sor_StartEndList[0][1]
    for i in range(n):
        if st <= sor_StartEndList[i][0]:
            cnt+=1
            st = sor_StartEndList[i][1]   

    return cnt

try:
    n = int(input())
    StartEndList = [list(map(int, input().split())) for _ in range(n)]
    print(calTimes(n,StartEndList))    

except Exception as e:
    traceback.print_exc()
    print("[ERROR]",e)