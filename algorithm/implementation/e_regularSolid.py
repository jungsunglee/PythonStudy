# N, M 정 다면체(4,6,8,12,20) 중 각각 숫자 1개 합이 가장 확률 높은 숫자 출력
import sys
sys.stdin = open("./algorithm/implementation/input.txt","rt")

raw_list = []
re_dict = dict()
N, M = map(int, input().split())
for a in range(1,N+1):
    for b in range(1,M+1):
        raw_list.append(a+b)
raw_list.sort()
for a in range(2,N+M+1):
    re_dict[a] = raw_list.count(a)

result = [ a for a, b in re_dict.items() if max(re_dict.values()) == b]
for i in result: print(i, end=' ')

#Solution : 별로임