# 1 ~ 20 오름차순 / 각 카드 위치는 카드에 적힌 숫자
# 카드위치 변경 규칙
# a. [a,b] 1<=a<=b<=20 -> a부터 b까지 카드 위치 현재의 역순
import sys, traceback

sys.stdin = open("./algorithm/string_1st_2nd_List/input.txt", "rt")

def reverseCard(a: int, b: int, cardList: list)->list:
    ref_list=cardList[a-1:b]
    ref_list.reverse()
    cnt = 0
    for i in range(a-1,b):
        cardList[i] = ref_list[cnt]
        cnt+=1
    return cardList

# Solution
def reverseCard_sol(a: int, b: int, cardList: list)->list:
    for i in range((b-a+1)//2):
       cardList[a+i-1], cardList[b-i-1] = cardList[b-i-1], cardList[a+i-1] # list 값 변경
    return cardList


try:
    cardList = list(range(1,21))
    for i in range(10):
        a,b = map(int, input().split())
        if (a or b) not in cardList:    
            raise Exception("The range of a,b is 1<= a,b <=20.")
        else:
            cardList = reverseCard_sol(a,b,cardList)
    print(" ".join(str(x) for x in cardList))
except Exception as e:
    traceback.print_exc()
    print("[ERROR]",e)