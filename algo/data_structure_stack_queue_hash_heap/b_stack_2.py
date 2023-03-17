# 쇠 막대기는 가지보다 긴 쇠막대기 위에만 위치함
# 끝 점은 겹치지 않게 위치
# 쇠 막대기 자르는 레이저는 적어도 하나 존재
# 레이저는 어떤 쇠막대기의 양 끝점과 겹치지 않음
# 쇠 막대기와 레이저의 배치 -> 괄호표 -> 잘려진 쇠막대기 조각의 총 개수
# 괄호 문자의 최대 개수는 100,0000
import sys, traceback

sys.stdin = open("./algorithm/data_structure_stack_queue_hash_heap/input.txt", "rt")

def cal_divNum(bracket:list)->int:
    res = 0
    stack = []
    for i in range(len(bracket)):
        if bracket[i] =="(":
            stack.append(i)
        elif bracket[i] ==")":
            if bracket[i-1] == "(":
                stack.pop()
                res += len(stack)
            else:
                stack.pop()
                res +=1
    return res

try:
    bracket = list(input())
    print(cal_divNum(bracket))
except Exception as e:
    traceback.print_exc()
    print("[ERROR]",e)