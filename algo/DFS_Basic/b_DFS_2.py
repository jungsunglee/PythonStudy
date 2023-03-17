import traceback

def DFS(n:int)->None:
    if n > 7:
        return
    else:
        # 전위 순회 출력
        print(n, end='')  
        DFS(2*n)
        DFS(2*n+1) 

        # 중위 순회 출력
        DFS(2*n)
        print(n, end='')
        DFS(2*n+1) 

        # 후위 순회 출력
        DFS(2*n)
        print(n, end='')
        DFS(2*n+1) 

try:    
    DFS(1)

except Exception as e:
    traceback.print_exc()
    print("[ERROR]",e)