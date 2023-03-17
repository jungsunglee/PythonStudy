# N면 지원자 / 키 몸무게 중 적어도 키가 크거나 무거운 지원자 합격
# A 지원자보다 키도 크고 몸무게 무거운 지원자가 있다면 A는 탈락
# 5<= N <= 50
import sys, traceback

sys.stdin = open("./algorithm/decision_greedy_algorithm/input.txt", "rt")

def selectPlayer(N:int, PlayerList:list)->int:
    cnt = 0
    Hc = Wc =0
    PlayerList.sort(key=lambda x: x[0],reverse=True)
    '''for i in range(N):
        #print(PlayerList[i])
        H,W = PlayerList[i]
        if H > Hc or W > Wc:
            cnt += 1
            Hc = H
            Wc = W'''
    for H,W in PlayerList:
        if H > Hc or W > Wc:
            cnt += 1
            Hc = H
            Wc = W

    return cnt

try:
    N = int(input())
    PlayerList = [list(map(int, input().split())) for _ in range(N)]
    print(selectPlayer(N,PlayerList))

except Exception as e:
    traceback.print_exc()
    print("[ERROR]",e)