import traceback,sys

def DFS(ch_dict:dict,cnt:int)->str:
    if n == cnt:
        b = 0
        a = 0
        for k,v in ch_dict.items():
            if v == 1:
                a +=k
            else:
                b +=k
        #print(a, end= ' ')
        #print(b)
        if a == b:
            print('YES')
            sys.exit(0)

    else:
        i = setList[cnt]
        ch_dict[i] = 1
        DFS(ch_dict, cnt+1)
        ch_dict[i] = 0
        DFS(ch_dict, cnt+1)

try:
    with open("./algo/DFS_Basic/input.txt","r") as f:
        n = int(f.readline().strip())
        setList = list(map(int, f.readline().strip().split()))
    ch_dict = dict()
    for i in setList:
        ch_dict[i] = 0
    cnt = 0
    DFS(ch_dict, cnt)
    print("NO")

except Exception as e:
    traceback.print_exc()
    print("[ERROR]",e)