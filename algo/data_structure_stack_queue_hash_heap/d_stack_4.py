# postfix 연산 : 352+*9- --> 12
import sys, traceback

sys.stdin = open("./algo/data_structure_stack_queue_hash_heap/input.txt", "rt")

def cal_postfix(postfix:list) -> int:
    res = 0
    stack = []
    for i in postfix:
        if i == "+":
            y = int(stack.pop())
            x = int(stack.pop())
            stack.append(x+y)
        elif i == "-":
            y = int(stack.pop())
            x = int(stack.pop())
            stack.append(x-y)
        elif i == "*":
            y = int(stack.pop())
            x = int(stack.pop())
            stack.append(x*y)
        elif i == "/":
            y = int(stack.pop())
            x = int(stack.pop())
            stack.append(x/y)
        else:
            stack.append(i)
    res = stack.pop()
    return res


try:
    postfix = list(input())
    print(cal_postfix(postfix))

except Exception as e:
    traceback.print_exc()
    print("[ERROR]",e)