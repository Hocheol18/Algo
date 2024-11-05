

def solution(input_data, target_floor, target_pos):
    # 각 층의 문자열을 숫자 리스트로 변환
    buildings = [list(map(int, floor.split(','))) for floor in input_data]
    
    # 각 층의 블록들이 차지하는 구간을 계산하는 함수
    def calculate_intervals(floor):
        intervals = []
        current_pos = 0
        for num in buildings[floor]:
            intervals.append((current_pos, current_pos + num))
            current_pos += num
        return intervals
    
    # 특정 구간이 다른 구간과 겹치는지 확인하는 함수
    def has_overlap(interval1, interval2):
        return not (interval1[1] <= interval2[0] or interval1[0] >= interval2[1])
    
    # 타겟 블록의 구간 찾기
    target_intervals = calculate_intervals(target_floor)
    target_interval = target_intervals[target_pos]
    
    total_sum = 0
    
    # 아래 층들을 순회하며 겹치는 블록들의 값을 더함
    for floor in range(target_floor + 1, len(buildings)):
        intervals = calculate_intervals(floor)
        for i, (start, end) in enumerate(intervals):
            if has_overlap(target_interval, (start, end)):
                total_sum += buildings[floor][i]
    
    return total_sum

# 테스트
input_data = ["1,2,7", "4,2,4", "1,1,1,1,4,2"]
print(solution(input_data, 0, 0))  # target_floor=0, target_pos=1 (값이 2인 위치)