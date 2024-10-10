def DFS(word, target):
    global num, answer

    if len(word) > 5:
        return
    
    num += 1

    if word == target:
        
        answer = num
        return
    
    DFS(word+'A', target)
    DFS(word+'E', target)
    DFS(word+'I', target)
    DFS(word+'O', target)
    DFS(word+'U', target)

def solution(word):
    global num, answer

    num, answer = 0, 0

    DFS('', word)
    return answer - 1
    