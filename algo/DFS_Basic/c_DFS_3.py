import traceback

def DFS(x:int):
    if x == n+1:
        for i in range(1,n+1):
            if checkList[i] ==1:
                print(i,end=' ')
        print()
    else:
        checkList[x] = 1
        DFS(x+1)
        checkList[x] = 0
        DFS(x+1)


try:
    with open("./algo/DFS_Basic/input.txt","r") as f:
        n = int(f.readline().strip())
    checkList = [0]*(n+1)
    DFS(1)
    

except Exception as e:
    traceback.print_exc()
    print("[ERROR]",e)