# OX 문제 -> 1문제 1점 / 연속으로 맞출 경우 2번째 문제는 2점 3번째문제는 3점 k번째 문제는 k점
# N(1<=N<=100)개 문제 / 두번째 줄 채점 결과
import sys

sys.stdin = open("./algorithm/implementation/input.txt", "rt")
N = int(input())
GradingList = list(map(int, input().split()))
cnt = 0
score = 0
for i in GradingList:
    if i ==0:
        cnt=0
    else:
        cnt+=1
    score = score + cnt

print(score)
