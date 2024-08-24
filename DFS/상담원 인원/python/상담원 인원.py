from itertools import product
from collections import deque

def dfs(one, two, three, doing_one, doing_two, doing_three, ans, reqs):
    one_time, two_time, three_time = 0,0,0
    
    for i in reqs:

        if i[2] == 1:
            if len(doing_one) < one:
                doing_one.append([i[0] + i[1], i[0], i[1]])
                doing_one.sort()
            else:
                one_time = doing_one.pop(0)[0]
                doing_one.append([one_time + i[1], i[0], i[1]])
                doing_one.sort()
                ans += one_time - i[0]
        elif i[2] == 2:
            if len(doing_two) < two:
                doing_two.append([i[0] + i[1], i[0], i[1]])
                doing_two.sort()
            else:
                two_time = doing_two.pop(0)[0]
                print(two_time)
                doing_two.append([two_time + i[1], i[0], i[1]])
                doing_two.sort()
                ans += two_time - i[0]
        elif i[2] == 3:
            if len(doing_three) < three:
                doing_three.append([i[0] + i[1], i[0], i[1]])
                doing_three.sort()
            else:
                three_time = doing_three.pop(0)[0]
                doing_three.append([three_time + i[1], i[0], i[1]])
                doing_three.sort()
                ans += three_time - i[0]

    return ans

def solution(k, n, reqs):
    answer = 1e9
    list_n = [i for i in range(1, n)]

    new_list = sorted(reqs, key=lambda x: x[0])

    m = list(product(list_n,repeat=k))
    for i in m:
        if sum(i) == n:
            ans = dfs(i[0], i[1], i[2], [],[],[], 0, new_list)

            if answer > ans:
                answer = ans
    return answer

print(solution(3,5, [[10, 60, 1], [15, 100, 3], [20, 30, 1], [30, 50, 3], [50, 40, 1], [60, 30, 2], [65, 30, 1], [70, 100, 2]]))