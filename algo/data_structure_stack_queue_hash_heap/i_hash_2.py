# Anagram : 두 문자열이 알파벳 나열 순서는 다르지만 구성이 일치 시 anagram
import traceback

def check_anagram(input_1:list, input_2:list)->str:
    res = ""
    in1_dict = dict()
    in2_dict = dict()
    for i in input_1:
        in1_dict[i] = input_1.count(i)
    
    for i in input_2:
        in2_dict[i] = input_2.count(i)
    
    if in1_dict == in2_dict:
        res = "YES"
    else:
        res = "NO"

        

    return res

try:
    with open("./algo/data_structure_stack_queue_hash_heap/input.txt","r") as f:
        input_1 = list(f.readline().strip())
        input_2 = list(f.readline().strip())
    print(check_anagram(input_1, input_2))

    
except Exception as e:
    traceback.print_exc()
    print('[ERROR]',e)