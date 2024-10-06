def logic(level, diffs, times, limit):
    total_time = 0
    for idx in range(len(diffs)):
        if diffs[idx] <= level:
            total_time += times[idx]
        else:
            total_time += (diffs[idx] - level) * (times[idx] + times[idx-1]) + times[idx]
            
    if total_time > limit:
        return False
    else:
        return True
    

def solution(diffs, times, limit):
    start, end = 1, max(diffs) + 1
    answer = 0
    
    while start <= end:
        mid = (start + end) // 2
        
        if logic(mid, diffs, times, limit):
            end = mid - 1
            answer = mid
        else:
            start = mid + 1
            
            
    return answer