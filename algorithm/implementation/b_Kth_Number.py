# N개 숫자열 중 S ~ e번쨰 까지의 수를 오름 차순 정리 
# k번째 숫자열 출력
'''
IN
Case : 1 <= C <= 10
N(5<=N<=500) s e k
숫자열

OUT
#CaseNumber 결과

'''
import sys

sys.stdin = open("./algorithm/implementation/input.txt", "rt")

CN = int(input())
cond = []
NL = []
for i in range(CN):
    Cs = list(map(int, input().split()))
    cond.append(Cs)
    Ns = list(map(int, input().split()))
    NL.append(Ns)

for i in range(1, CN+1):
    C = cond[i-1]
    Ns = NL[i-1]
    if C[0] == len(Ns):
        Ns = sorted(Ns[C[1]-1:C[2]])
        re = Ns[C[3]-1]
        print(f"#{i} {re}")
    else:
        break

# Solution
CN = int(input())
for i in range(CN):
    n, s, e, k = map(int, input().split())
    Ns = list(map(int, input().split()))
    Ns = Ns[s-1:e]
    Ns.sort()
    print(f"#{i+1} {Ns[k-1]}")
