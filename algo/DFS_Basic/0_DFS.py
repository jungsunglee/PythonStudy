import traceback

def DFS(x:int):
    if x > 0:
        print(x, end=' ') # 3 2 1로 출력됨
        DFS(x-1)
        print(x, end=' ') # 1 2 3으로 출력됨
        # print의 위치에 따라서 출력되는 결과의 순서가 변경되는 이유 : stack을 사용하기 때문

if __name__ == "__main__":
    try:
        with open("./algo/DFS_Basic/input.txt","r") as f:
            n = int(f.readline().strip())
            DFS(n)
            
    except Exception as e:
        traceback.print_exc()
        print("[ERROR]",e)
