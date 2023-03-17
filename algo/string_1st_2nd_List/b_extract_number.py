# 문자 + 숫자 = 문자열에서 숫자만 추출
# 0 0 1 2 0 -> 자연수로 변경 120 출력 -> 약수의 갯수 출력
# 자연수 >= 100,000,000 / 문자열 <= 50
import sys, traceback

sys.stdin = open("./algorithm/string_1st_2nd_List/input.txt", "rt")

# Solution
def extract_number_sol(InStr: str) -> int:
    res = 0
    for i in InStr:
        if i.isdecimal():
            res = res*10+int(i) # 이 공식 유용함.
    return res

def extract_number(InStr: str) -> int:
    numStr = ''
    for i in InStr:
        if i.isdecimal(): # 0 ~ 9까지 숫자는 isdecimal이 적합 / isDigit은 2^2 2^31 같을 숫자도 True로 return함.
            numStr += i
    return int(numStr)

def cal_divisor(number: int) -> int:
    cnt = 0
    for i in range(1,number+1):
        if number%i==0:
            cnt+=1
    return cnt
        
try:
    InStr = input()
    if len(InStr) >50:
        raise Exception("The length of string could not exceed 50.")
    else:
        number = extract_number(InStr)
        cntDivisor = cal_divisor(number)
        print(number,cntDivisor, sep='\n')

except Exception as e:
    traceback.print_exc()
    print("[ERROR]",e)