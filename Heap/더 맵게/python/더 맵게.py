import heapq

def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville)
    
    while len(scoville) >= 1:
        first = heapq.heappop(scoville)
        if len(scoville) == 0:
            if first >= K:
                return answer
            return -1
        if first >= K:
            return answer
        first += 2 * heapq.heappop(scoville)
        heapq.heappush(scoville, first)
        answer += 1

    return -1