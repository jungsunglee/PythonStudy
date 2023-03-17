# 순서 유지 -> 가장큰수 : 5276823 -> 3개 자릿수 제거 -> 7823
import sys, traceback

sys.stdin = open("./algorithm/data_structure_stack_queue_hash_heap/input.txt", "rt")

def cal_max(num:int, m:int) -> int:
    res = ''
    numList = list(str(num))
    stack = []
    for i in numList:
        while stack and m != 0 and stack[-1] < i:
            stack.pop()
            m -= 1
        stack.append(i)    
    
    if m != 0:
        stack = stack[:-m]
    
    res = ''.join(x for x in stack)
    return res

try:
    num, m = map(int, input().split())
    print(cal_max(num,m))

except Exception as e:
    traceback.print_exc()
    print("[ERROR]",e)