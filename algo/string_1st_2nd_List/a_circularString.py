### 이거 한번 더 풀어보기
# N(1<=N<20)개 문자열 앞뒤에서 읽을때 같은 문자 검사
import traceback
import sys

sys.stdin = open("./algorithm/string_1st_2nd_List/input.txt", "rt")

def checkCirStr(cnt:int)->None:
    for i in range(1,cnt+1):
        cirStr = input()
        cirStr_reverse = cirStr[::-1] #이거 중요
        if cirStr.lower() == cirStr_reverse.lower():
            print(f"#{i} YES")
        else:
            print(f"#{i} NO")

# Solution
def checkCirStr_sol(cnt:int)->None:
    for i in range(1,cnt+1):
        cirStr = input()
        cirStr = cirStr.lower()
        for j in range(len(cirStr)//2):
            if cirStr[j]!=cirStr[-1-j]: 
                #문자열 슬라이싱 역순으로 접근하는 방식
                print(f"#{i} NO")
                break
            else:
                print(f"#{i} YES")
                break
            
try:
    N = int(input())
    if 1<=N<=20:
        checkCirStr(N)       
    else:
        raise Exception("Please input the right range of number")

except ValueError as e:
    traceback.print_exc()
    print("[ERROR]",e)

except Exception as e:
    traceback.print_exc()
    print("[ERROR]",e)

        