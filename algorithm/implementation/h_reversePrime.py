# N(3<=N<=100)개 자연수 입력 -> 자연수 reverse가 소수이면 그 수 출력
# 첫자리부터 연속된 0은 무시
# 각 자연수의 크기는 100,000을 넘지 않음
import sys
import traceback

#Solution
def reverse_sol(number: int)-> int:
    res = 0
    while number > 0: # 몫이 0이면 stop 즉, 나뉘는 수가 10보다 작으면 stop
        remainder = number%10
        res = res*10+remainder
        number = number//10
    return res

def isPrime_sol(reverseNum: int)-> bool:
    if reverseNum == 1:
        return False
    for i in range(2,i//2+1): # 소수는 1과 자기 자신을 약수로 갖는 수로 그 숫자의 절반까지만 확인하면 됨.
        if reverseNum%i==0:
            return False
    else:
        return True

def reverse(number: int)->int:
    re = []
    while True:
        quotient = number//10
        remainder = number%10
        if quotient <10:
            re.append(remainder)
            re.append(quotient)
            break
        elif remainder == 0 and quotient < 10:
            re.append(quotient)
            break
        elif remainder == 0 and quotient >=10 and len(re) ==0:
            number = quotient
        elif remainder == 0 and quotient >=10 and len(re) !=0:
            re.append(remainder)
            number = quotient
        elif remainder != 0:
            re.append(remainder)
            number = quotient
    return int(''.join(str(a) for a in re))

def isPrime(reverseNum:int)->bool:
    cnt = 0
    for i in range(1, reverseNum+1):
        if reverseNum%i==0:
            cnt +=1
    if cnt == 2:
        return True
    else:
        return False

sys.stdin = open("./algorithm/implementation/input.txt", "rt")
try:
    N = int(input())
    inList = list(map(int, input().split()))
    if N <3 or N >100:
        raise Exception("There is wrong range of the number of count(3<=N<=100)")
    for i in inList:
        if i >100000:
            raise Exception("The input number could not exceed 100,000")
    
    for a in inList:
        if a >=10:
            reverseNum = reverse(a)
        else:
            reverseNum = a
        rePrime = isPrime(reverseNum)
        if rePrime == True:
            print(reverseNum, end=" ")

except Exception as e:
    print(traceback.print_exc())
    print("[ERROR] ", e)