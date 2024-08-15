def solution(h1, m1, s1, h2, m2, s2):
    now_time = h2 * 3600 + m2 * 60 + s2
    answer = 0
    ph, pm, ps = h1 % 12 * 3600 * 0.0083333 + m1 * 60 * 0.0083333 + s1 * 0.0083333, m1 * 60 * 0.1 + s1 * 0.1, s1 * 6
    
    for time_ in range(h1 * 3600 + m1 * 60 + s1 , h2 * 3600 + m2 * 60 + s2 + 1):

        h, m, s = time_ // 3600, time_ % 3600 // 60, time_ % 3600 % 60
        time = h % 12 * 3600 * 0.0083333 + m * 60 * 0.0083333 + s * 0.0083333
        minute = m * 60 * 0.1 + s * 0.1
        second = s * 6

        if time == 0: time = 360
        if minute == 0: minute = 360
        if h1 * 3600 + m1 * 60 + s1 != time_:
            if second == 0: second = 360
        
        if time_ == 43200 or time_ == 0:
            answer += 1 
        else:   
            if second >= minute:
                if pm > ps:
                    answer += 1
                
            if second >= time:
                if ph > ps:
                    answer += 1
                
        ph, pm, ps = time, minute, second

        if ph == 360: ph = 0
        if pm == 360: pm = 0
        if ps == 360: ps = 0

        if time_ >= now_time:
            break

    return answer