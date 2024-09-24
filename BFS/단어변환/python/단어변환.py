from collections import deque

def solution(begin, target, words):
    queue = deque()
    queue.append([begin, 0])
    
    if target not in words:
        return 0
    
    while queue:
        begin, answer = queue.popleft()
        if begin == target:
            return answer
        for word in words:
            cnt = 0
            for i in range(len(word)):
                if word[i] == begin[i]:
                    cnt += 1
            if cnt == len(word) - 1:
                queue.append([word, answer + 1])
                