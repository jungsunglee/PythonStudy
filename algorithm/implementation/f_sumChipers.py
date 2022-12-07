# N개 자연수 -> 각 자연수 자릿수의 합이 최대인 자연수 출력
# def digit_sum(x) 꼭 사용
import sys

sys.stdin = open("./algorithm/implementation/input.txt", "rt")
N = int(input())
digit_L = list(map(int, input().split()))

def digit_sum(digit_L: list) -> int:
    re, sum_max = 0, 0
    for a in digit_L:
        sum = 0
        str_a = str(a)
        for b in str_a: 
            sum += int(b)
        if sum > sum_max:
            sum_max = sum
            re = a
    return re

# Solution
def digit_sum_sol(digit_L: list) -> int:
    re, sum_max = 0, 0
    for a in digit_L:
        ori_a = a
        sum = 0
        #아래와 같은 방식으로 구현       
        while a > 0:
            sum+=a%10
            a=a//10
        #########################
        if sum > sum_max:
            sum_max = sum
            re = ori_a
    return re

try:
    if N != len(digit_L):
        raise Exception("Please Input the right number of values")
    print(digit_sum_sol(digit_L))

except Exception as e:
    print("[ERROR] ",e)