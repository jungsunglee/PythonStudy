# INPUT
# 첫줄 : 필수과목
# 두번째 줄 : 수업설계 수
# 세번째 줄 : 작성한 수업 설계

# OUTPUT
# 잘된 것이면 #1 YES 잘못된 것이면 #1 NO

import sys, traceback
from collections import deque

sys.stdin = open("./algo/data_structure_stack_queue_hash_heap/input.txt", "rt")

def check_ans(sol:str, ans:deque) -> str:
    res = ''
    res_list=[]

    for _ in range(len(ans)):
        cur = ans.popleft()
        if cur in sol:
            ans.append(cur)

    for i in ans:
        if i not in res_list:
            res_list.append(i)

    if sol == ''.join(x for x in res_list):
        res = "YES"
    else:
        res = "NO"
    return res

try:
    sol = input()
    cnt = int(input())
    for i in range(1,cnt+1):
        ans = deque(input())
        print(f'#{i} ' + check_ans(sol,ans))
except Exception as e:
    traceback.print_exc()
    print("[ERROR]",e)