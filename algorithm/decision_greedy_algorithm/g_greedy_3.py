# 창고 가로 7 / 1열 : 6개 상자, 2열 : 3개 상자, 3열 : 9개 상자
# 높이 조정 : 가장 높은 곳 상자를 가장 낮은 곳으로 이동 -> 여러 곳이면 그 중 아무거나 선택
# M회 높이 조정 후 가장 높은 곳과 가장 낮은 곳의 차이 출력
# L : 가로 길이 1<=L<=100
# M : 높이 조정 횟수 1<=M<=1,0000
import sys, traceback

sys.stdin = open("./algorithm/decision_greedy_algorithm/input.txt", "rt")

def calDiff(L:int, LH_List:list, M:int)->int:
    diff = 0
    
    for _ in range(M):
        LH_List.sort()
        LH_List.insert(0,LH_List.pop(0)+1)
        LH_List.append(LH_List.pop()-1)
        
    LH_List.sort()
    diff = LH_List[-1] - LH_List[0]

    return diff

try:
    L = int(input())
    LH_List = list(map(int, input().split()))
    M = int(input())
    print(calDiff(L,LH_List,M))


except Exception as e:
    traceback.print_exc()
    print("[ERROR]",e)