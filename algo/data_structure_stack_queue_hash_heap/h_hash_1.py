# N개 단어 -> 사용하지 않은 단어 찾기
import sys, traceback

sys.stdin = open("./algo/data_structure_stack_queue_hash_heap/input.txt", "rt")

def find_unuse(dic_willuse:dict, dic_use:dict) -> str:
    for u in dic_use:
        for wu in dic_willuse:
            if dic_use[u] == dic_willuse[wu]:
                del dic_willuse[wu]
                break
    
    for i in dic_willuse.values():
        res = i
    return res

try:
    N = int(input())
    #dic_willuse = dict((num, var) for num, var in enumerate(input() for _ in range(N)))
    #dic_use = dict((num, var) for num, var in enumerate(input() for _ in range(N-1)))
    #print(find_unuse(dic_willuse, dic_use))

    # sol
    p = dict()
    for i in range(N):
        w = input()
        p[w] = 0
    for i in range(N-1):
        w = input()
        p[w] = 1
    for i in p:
        if p[i] == 0:
            print(i)
            break

    

except Exception as e:
    traceback.print_exc()
    print("[ERROR]",e)