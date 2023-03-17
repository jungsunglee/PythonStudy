# 10진수 N -> 2진수로 변환
import traceback

def dfs_conv_bin(n:int)->int:
    if n >0:
        dfs_conv_bin(n//2)
        print(n%2, end='')

try:
    with open("./algo/DFS_Basic/input.txt","r") as f:
        n = int(f.readline().strip())
    dfs_conv_bin(n)

except Exception as e:
    traceback.print_exc()
    print("[ERROR]",e)