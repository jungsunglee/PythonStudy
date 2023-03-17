# N(2<=N<=1000)명 사람들 참여 -> 3개 주사위 던뎌 아래 규칙으로 가장 많은 상금을 출력
# R1 같은 수 3개 -> 10,000원 + dice_num*1,000원
# R2 같은 수 2개 -> 1,000원 + dice_num*100원
# R3 모두 다른 수 -> large_dice_num*100원
import sys
import traceback

def cal_cash(raw: list)-> int:
    for i in raw[0:1]:
        if raw.count(i) == 3:
            return 10000+i*1000
        elif raw.count(i) ==2:
            return 1000+i*100
        else:
            return max(raw)*100

sys.stdin = open("./algorithm/implementation/input.txt", "rt")
try:
    diceRe = []
    N = int(input())
    for i in range(N):
        raw=list(map(int, input().split()))
        diceRe.append(cal_cash(raw))
    print(max(diceRe))
    

except Exception as e:
    traceback.print_exc()
    print("[ERROR] ", e)