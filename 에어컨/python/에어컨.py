from collections import deque

def solution(outside_temp, t1, t2, a, b):
    # 초기 상태: 실외온도와 현재 온도는 동일
    queue = deque([(0, outside_temp, False, 0)])  # (현재 시간, 현재 온도, 에어컨 상태, 소비 전력)
    visited = set()
    visited.add((0, outside_temp, False))
    
    min_power = float('inf')
    
    while queue:
        time, current_temp, ac_on, power = queue.popleft()
        
        # 현재 온도가 t1 ~ t2 사이에 있고 에어컨이 켜져 있을 경우
        if t1 <= current_temp <= t2 and ac_on:
            min_power = min(min_power, power)
            continue
        
        # 다음 상태로 가는 경우를 고려
        # 1. 에어컨이 켜져 있는 경우
        if ac_on:
            if current_temp < t2:
                # 희망온도가 더 높은 경우
                next_temp = current_temp + 1
                next_power = power + a
                if (time + 1, next_temp, True) not in visited:
                    visited.add((time + 1, next_temp, True))
                    queue.append((time + 1, next_temp, True, next_power))
                    
            if current_temp > t1:
                # 희망온도가 더 낮은 경우
                next_temp = current_temp - 1
                next_power = power + a
                if (time + 1, next_temp, True) not in visited:
                    visited.add((time + 1, next_temp, True))
                    queue.append((time + 1, next_temp, True, next_power))
                    
            # 희망온도와 같다면 b만큼 소비
            if t1 <= current_temp <= t2:
                next_temp = current_temp
                next_power = power + b
                if (time + 1, next_temp, True) not in visited:
                    visited.add((time + 1, next_temp, True))
                    queue.append((time + 1, next_temp, True, next_power))
        
        # 2. 에어컨이 꺼져 있는 경우
        if not ac_on:
            if current_temp < outside_temp:
                next_temp = current_temp + 1
                if (time + 1, next_temp, False) not in visited:
                    visited.add((time + 1, next_temp, False))
                    queue.append((time + 1, next_temp, False, power))
                    
            if current_temp > outside_temp:
                next_temp = current_temp - 1
                if (time + 1, next_temp, False) not in visited:
                    visited.add((time + 1, next_temp, False))
                    queue.append((time + 1, next_temp, False, power))
        
        # 3. 에어컨을 켜는 경우
        if not ac_on:
            if (time + 1, current_temp, True) not in visited:
                visited.add((time + 1, current_temp, True))
                queue.append((time + 1, current_temp, True, power))
                
        # 4. 에어컨을 끄는 경우
        if ac_on:
            if (time + 1, current_temp, False) not in visited:
                visited.add((time + 1, current_temp, False))
                queue.append((time + 1, current_temp, False, power))
    
    return min_power

# 예시 실행
print(solution(28, 18, 26, 10, 8))