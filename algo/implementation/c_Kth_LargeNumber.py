# N(3<=N<=100)장의 카드 중 3장을 뽑아 더함.
# 더한 값 중 K(1<=K<=50)번째 큰수
# 더한 값들이 중복될 경우 삭제
import sys

sys.stdin=open("./algorithm/implementation/input.txt","rt")
N, k = map(int,input().split())
v = list(map(int, input().split()))
v.sort(reverse=True)
sumList = []
if len(v)==N:
    for a in range(N):
        for b in range(a+1,N):
            for c in range(b+1,N):
                sum = v[a] + v[b] + v[c]
                sumList.append(sum)
sumList = sorted(list(set(sumList)),reverse=True)
print(sumList[k-1])

#Soultion
N, k = map(int,input().split())
v = list(map(int, input().split()))
sumSet = set() #set을 처음부터 선언하여 중복을 방지
if len(v)==N:
    for a in range(N):
        for b in range(a+1,N):
            for c in range(b+1,N):
                sumSet.add(v[a] + v[b] + v[c]) # add를 사용하여 set에 값을 추가시 중복된 값은 넣지 않음
result = sorted(list(sumSet), reverse=True)
print(result[k-1])

