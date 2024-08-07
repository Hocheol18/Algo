from collections import defaultdict

def solution(friends, gifts):
    pr_ratio = [0 for _ in range(len(friends))] 
    records = [[0 for _ in range(len(friends))] for _ in range(len(friends))]
    presents = [0 for _ in range(len(friends))] 
    friend = {}

    for index in range(len(friends)):
        friend[friends[index]] = index
            
    for gift in gifts:
        a, b = gift.split()
        records[friend[a]][friend[b]] += 1
        pr_ratio[friend[a]] += 1
        pr_ratio[friend[b]] -= 1

    for y in range(len(friends)):
        for x in range(y+1, len(friends)):
            if records[y][x] == 0:
                if records[x][y] == 0:
                    if pr_ratio[y] > pr_ratio[x]:
                        presents[y] += 1
                    elif pr_ratio[x] > pr_ratio[y]:
                        presents[x] += 1
                elif records[x][y] > 0:
                    presents[x] += 1
            elif records[y][x] > 0:
                if records[x][y] > records[y][x]:
                    presents[x] += 1
                elif records[y][x] > records[x][y]:
                    presents[y] += 1
                elif records[y][x] == records[x][y]:
                    if pr_ratio[y] > pr_ratio[x]:
                        presents[y] += 1
                    elif pr_ratio[x] > pr_ratio[y]:
                        presents[x] += 1
    
    return max(presents)