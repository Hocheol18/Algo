# from collections import deque

# def solution(n):
#     queue = deque([(0, "", 0)])
#     visited = set()

#     while queue:
#         ans, string, i = queue.popleft()

#         if ans == n:
#             print(string)
#             exit()

#         if i > 30:  # 깊이 제한
#             continue
        
#         if (ans, i) in visited:
#             continue
#         visited.add((ans, i))

#         queue.append([ans + (-2) ** i , "1" + string, i+1])
#         queue.append([ans, "0" + string, i+1])


# solution(int(input()))



n = int(input())
if n == 0:
    print("0")
else:
    answer = ""
    while n != 0:
        remainder = n % -2
        n //= -2

        if remainder < 0:
            remainder += 2
            n += 1
        
        answer = str(remainder) + answer

    print(answer)
