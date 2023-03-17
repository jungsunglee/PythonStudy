# N, M(1<=N<=100) 리스트 크기 / 오름차순 리스트
# int형 변수의 크기를 넘지 않음 int형 변수 크기 = 4 bytes = 8bit *4 = 32 bit
import sys, traceback

sys.stdin = open("./algorithm/string_1st_2nd_List/input.txt", "rt")

try:
    N = int(input())
    NList = list(map(int, input().split()))    
    M = int(input())
    MList = list(map(int, input().split()))
    #print(" ".join(str(a) for a in sorted(NList + MList)))

    #Solution sort()사용하지 않고 풀기
    P1 = P2 = 0 # 다중 변수에 동일한 값 입력
    reList = []
    while P1<N and P2<M:
        if NList[P1] < MList[P2]:
            reList.append(NList[P1])
            P1+=1
        else:
            reList.append(MList[P2])
            P2+=1
    if P1 <N:
        reList = reList + NList[P1:]
    elif P2<M:
        reList = reList + MList[P2:]
    print(" ".join(str(a) for a in reList))


except Exception as e:
    traceback.print_exc()
    print("[ERROR]",e)