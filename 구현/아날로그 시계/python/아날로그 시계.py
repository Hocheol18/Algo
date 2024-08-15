# 0.00833333 도
# 0.1 도
# 6 도

def solution(h1, m1, s1, h2, m2, s2):
    now_time = h2 * 3600 + m2 * 60 + s2
    answer = 0
    ph, pm, ps = h1 % 12 * 3600 * 0.0083333 + m1 * 60 * 0.0083333 + s1 * 0.0083333, m1 * 60 * 0.1 + s1 * 0.1, s1 * 6
    print(ph, pm, ps)
    for time_ in range(h1 * 3600 + m1 * 60 + s1 , h2 * 3600 + m2 * 60 + s2 + 1):

        h, m, s = time_ // 3600, time_ % 3600 // 60, time_ % 3600 % 60
        time = h % 12 * 3600 * 0.0083333 + m * 60 * 0.0083333 + s * 0.0083333
        minute = m * 60 * 0.1 + s * 0.1
        second = s * 6

        if time == 0: time = 360
        if minute == 0: minute = 360
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

        print(time, minute, second, answer)

        if ph == 360: ph = 0
        if pm == 360: pm = 0
        if ps == 360: ps = 0

        if time_ >= now_time:
            break

    return answer

print(solution(0,59,0,1,0,1))

def solution2(h1, m1, s1, h2, m2, s2):
    def get_times(h, m, s):
        seconds = h * 60 * 60 + m * 60 + s

        sd = (s * 6) % 360
        md = (m * 6 + s * 0.1) % 360
        hd = (h * 30 + m * 0.5 + s * 0.5 / 60) % 360

        ret = (h * 60 + m) * 2 - h

        if sd >= md:
            ret += 1
        if sd >= hd:
            ret += 1

        if h >= 12:
            ret -= 2

        return ret

    ret = get_times(h2, m2, s2) - get_times(h1, m1, s1)

    if h1 in [0, 12] and m1 == 0 and s1 == 0:
        ret += 1

    return ret

print(solution2(0,59,0,1,0,1))