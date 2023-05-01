import heapq

def solution(n, works):
    if n > sum(works):   # 남은 작업량이 없으므로 0을 return한다
        return 0
    heap = []
 # heappush : heap에 원소 추가 
    for i in works:
        heapq.heappush(heap,-i) 
    for i in range(n):
        heapq.heappush(heap,heapq.heappop(heap)+1)
    return sum([i**2 for i in heap])
