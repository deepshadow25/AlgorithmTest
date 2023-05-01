import heapq

def solution(n, works):
    if n > sum(works):
        return 0
    heap = []
    for i in works:
        heapq.heappush(heap,-i)
    for i in range(n):
        heapq.heappush(heap,heapq.heappop(heap)+1)
    return sum([i**2 for i in heap])