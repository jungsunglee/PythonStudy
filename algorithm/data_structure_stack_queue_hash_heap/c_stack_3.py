# 후위표현식 3+5+*2 -> 352*+ / (3+5)*2 -> 35+2*
# 3+5*2/(7-2) --> 352*72-/+
# 3*(5+2)-9 --> 352+*9-
import sys, traceback

sys.stdin = open("./algorithm/data_structure_stack_queue_hash_heap/input.txt", "rt")

def chPostfix(infix:list) -> str:
    res = ''
    stack = []
    stack_res = []
    for i in infix:
        if i == '*' or i =='/':
            if stack and (stack[-1] == '*'or stack[-1] == '/'):
                stack_res.append(stack.pop())
                stack.append(i)
            else:
                stack.append(i)
        elif i == '+' or i == '-':
            if stack and (stack[-1] == '+'or stack[-1] == '-'):
                stack_res.append(stack.pop())
                stack.append(i)
            elif stack and (stack[-1] == '*'or stack[-1] == '/'):
                while stack:
                    stack_res.append(stack.pop())
                stack.append(i)
            else:
                stack.append(i)
        elif i == ')':
            while True:
                x = stack.pop()
                if x != '(':
                    stack_res.append(x)
                else:
                    break                
        elif i == '(':
            stack.append(i)       
        else:
            stack_res.append(i)
    stack_res = stack_res + stack[::-1]

    res = ''.join(i for i in stack_res)
    return res

def chPostfix_sol(infix:list) -> str:
    res = ''
    stack = []
    
    for i in infix:
        if i.isdecimal():
            res +=i

        elif i == '*' or i =='/':
            if stack and (stack[-1] == '*'or stack[-1] == '/'):
                stack_res.append(stack.pop())
                stack.append(i)
            else:
                stack.append(i)
        elif i == '+' or i == '-':
            if stack and (stack[-1] == '+'or stack[-1] == '-'):
                stack_res.append(stack.pop())
                stack.append(i)
            elif stack and (stack[-1] == '*'or stack[-1] == '/'):
                while stack:
                    stack_res.append(stack.pop())
                stack.append(i)
            else:
                stack.append(i)
        elif i == ')':
            while True:
                x = stack.pop()
                if x != '(':
                    stack_res.append(x)
                else:
                    break                
        elif i == '(':
            stack.append(i)       
        else:
            stack_res.append(i)
    stack_res = stack_res + stack[::-1]

    res = ''.join(i for i in stack_res)
    return res

try:
    infix = list(input())
    print(chPostfix(infix))

except Exception as e:
    traceback.print_exc()
    print("[ERROR]",e)