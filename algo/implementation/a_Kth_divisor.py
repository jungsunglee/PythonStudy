# a의 약수 중 b번째 약수 출력
# if b번째 약수가 존재하지 않으면 -1 출력

dL = []
a,b = map(int, input().split())
for i in range(1,a+1):
    if a%i == 0:
        dL.append(i)
if len(dL) < b: re = -1
else: re = dL[b-1]
print(re)

# Solution
a,b = map(int, input().split())
cnt = 0
for a in range(1, a+1):
    if a%i == 0: cnt += 1
    if cnt == b: # 이 조건을 사용하여 모든 약수를 계산하지 않아도 됨.
        print(i)
        break
else: # for ~ else 구문
    print(-1)