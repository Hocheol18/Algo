from itertools import product

def logic(doing_one, one, i, ans, one_time):
    if len(doing_one) < one:
        doing_one.append([i[0] + i[1], i[0], i[1]])
        doing_one.sort()
    else:
        one_time = doing_one.pop(0)[0]
        if one_time + i[1] < i[0] + i[1]:
            doing_one.append([i[0] + i[1], i[0], i[1]])
        else:
            doing_one.append([one_time + i[1], i[0], i[1]])
            ans += one_time - i[0]
        doing_one.sort()
        
    return ans

def dfs(one, two, three, four, five, doing_one, doing_two, doing_three, doing_four, doing_five, ans, reqs):
    one_time, two_time, three_time, four_time, five_time = 0,0,0,0,0
    
    for i in reqs:
       
        if i[2] == 1:
            ans = logic(doing_one, one, i, ans, one_time)
        elif i[2] == 2:
            ans = logic(doing_two, two, i, ans, two_time)
        elif i[2] == 3:
            ans = logic(doing_three, three, i, ans, three_time)
        elif i[2] == 4:
            ans = logic(doing_four, four, i, ans, four_time)
        elif i[2] == 5:
            ans = logic(doing_five, five, i, ans, five_time)

    return ans

def solution(k, n, reqs):
    answer = 1e9
    list_n = [i for i in range(1, n)]
    new_list = sorted(reqs, key=lambda x: x[0])
    if n == 1:
        list_n = [1]
    
    m = list(product(list_n, repeat=k))
    
    
    for i in m:
        if sum(i) == n:
            a,b,c,d,e = 0, 0, 0, 0, 0
            if len(i) == 1:
                a = i[0]
            elif len(i) == 2:
                a, b = i[0], i[1]
            elif len(i) == 3:
                a, b, c = i[0], i[1], i[2]
            elif len(i) == 4:
                a, b, c, d = i[0], i[1], i[2], i[3]
            else:
                a,b,c,d,e = i[0], i[1], i[2], i[3], i[4]
                
            ans = dfs(a,b,c,d,e, [],[],[],[],[], 0, new_list)

            if answer > ans:
                answer = ans
    return answer


## 최적화 코드
import heapq
from itertools import product

def logic(doing_one, one, i, ans):
    if len(doing_one) < one:
        heapq.heappush(doing_one, i[0] + i[1])
    else:
        one_time = heapq.heappop(doing_one)
        if one_time + i[1] < i[0] + i[1]:
            heapq.heappush(doing_one, i[0] + i[1])
        else:
            heapq.heappush(doing_one, one_time + i[1])
            ans += one_time - i[0]
        
    return ans

def dfs(groups, reqs):
    ans = 0
    doing = [[] for _ in range(len(groups))]
    
    for i in reqs:
        group_idx = i[2] - 1
        ans = logic(doing[group_idx], groups[group_idx], i, ans)
    
    return ans

def solution(k, n, reqs):
    answer = 1e9
    list_n = [i for i in range(1, n)]
    new_list = sorted(reqs, key=lambda x: x[0])

    if n == 1:
        list_n = [1]
    
    m = list(product(list_n, repeat=k))
    
    for i in m:
        if sum(i) == n:
            ans = dfs(i, new_list)
            if answer > ans:
                answer = ans
                
    return answer