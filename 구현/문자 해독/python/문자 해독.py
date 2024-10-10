import sys
import copy

a,b = map(int, sys.stdin.readline().split())
W = sys.stdin.readline().strip()
S = sys.stdin.readline().strip()
answer = 0

cnt = {}
for i in W:
    if i not in cnt:
        cnt[i] = 1
    else:
        cnt[i] += 1

def logic(word):
    global answer
    for i in box:
        i[word] -= 1
        
        if i[word] < 0:
            continue
        
        answer += 1
        for _, value in i.items():
            if value != 0:
                answer -= 1
                break

box = []
for word in S:
    if word in W:
        cnt_ = copy.deepcopy(cnt)
        box.append(cnt_)
        logic(word)
    else:
        box = []

print(answer)