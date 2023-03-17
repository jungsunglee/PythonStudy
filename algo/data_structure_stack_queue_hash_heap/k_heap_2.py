# 최대힙
import sys, traceback
import heapq as hq

try:
    heap = []
    with open("./algo/data_structure_stack_queue_hash_heap/input.txt","r") as f:
        while True:
            i = int(f.readline().strip())
            if i == -1:
                break
            elif i == 0:
                if len(heap) == 0:
                    print(-1)
                else:
                    print(-hq.heappop(heap))
            else:
                hq.heappush(heap,-i)

except Exception as e:
    traceback.print_exc()
    print("[ERROR]",e)