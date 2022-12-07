# N명 학생(5<=N<=100) 수학점수 평균(모든 값은 소수 첫째자리 반올림)
# 평균에 가장 가까운 학생이 몇 번째 인지 구함.
# 점수가 높은 학생 > 학생 번호가 빠른 학생
import sys

sys.stdin = open("./algorithm/implementation/input.txt","rt")

N = int(input())
#list로 받아온 값을 dict로 변경하는 code Comprehension 활용
scoreDict = {a:b for a,b in enumerate(list(map(int,input().split())),start=1)}
#scoreDict = {i+1 : scoreList[i] for i in range(N)}

scoreDict_diff = dict()
if len(scoreDict) == N:
    avg = round(sum(scoreDict.values())/N)
    for i in range(1, N+1):
        scoreDict_diff[i] = scoreDict[i] - avg
    #dic에서 최소 절대값의 key를 list로 구하는 code Comprehension 활용
    abs_min_list = [a for a,b in scoreDict_diff.items() if abs(min(scoreDict_diff.values(), key=abs)) == abs(b)]
    if len(abs_min_list) == 1:
        print(avg, abs_min_list[0])
    else:
        min_list = [a for a in abs_min_list if scoreDict[a] >=avg]
        print(avg, min_list[0])

#Solution
N = int(input())
List = list(map(int, input().split()))
avg = round(sum(list)/N)
min = 99999999
for id, x in enumerate(List):
    absV = abs(x-avg)
    if absV < min:
        min = absV
        score = x
        result = id +1
    elif absV == min:
        if x > score:
            score = x
            result = id +1

