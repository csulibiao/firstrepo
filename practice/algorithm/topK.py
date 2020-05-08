from queue import PriorityQueue
from typing import List, Any
import heapq
import random

bigdata = random.sample(range(100), 20)
print(bigdata)
print(sorted(bigdata, reverse=True))


def findTopK1(bigdata: List[int], k: int) -> Any:
    if k < 1:
        return None
    q = PriorityQueue(k)
    for value in bigdata:
        if q.qsize() < k:
            q.put(value)
        else:
            cur = q.get()
            q.put(value if value > cur else cur)
    return q.get()


def findTopK2(bigdata: List[int], k: int) -> Any:
    if k < 1:
        return None
    hq = bigdata[:k]
    heapq.heapify(hq)
    for item in bigdata[k:]:
        heapq.heappushpop(hq, item)
    return hq[0]


def findTopK3(bigdata: List[int], k: int) -> Any:
    tmp = bigdata[:k]
    tmp.sort(reverse=True)
    for item in bigdata[k:]:
        if item > tmp[-1]:
            tmp.pop()
            tmp.append(item)
            tmp.sort(reverse=True)
    return tmp[-1]

k = 6
print(f'Pq method, the {k}th largest number is:', findTopK1(bigdata, 6))
print(f'Hp method, the {k}th largest number is:', findTopK2(bigdata, 6))
print(f'Bf method, the {k}th largest number is:', findTopK3(bigdata, 6))
