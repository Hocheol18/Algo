from collections import deque

def solution(temperature, t1, t2, a, b, onboard):
    ans = 1e9
    
    queue = deque()
    queue.append([0, temperature, 0])

    while queue:
        index, nowtem, answer = queue.popleft()


        if (onboard[index] == 0 or (onboard[index] == 1 and (t1 <= nowtem <= t2))) and index == len(onboard) - 1:
            print(answer)
            ans = min(answer, ans)

        if index == len(onboard) - 1:
            continue
        
        if onboard[index] == 1 and (nowtem > t2 or nowtem < t1):
            continue
            
        # 세 케이스
        # 끄는 경우, 유지하는 경우, 에어컨 가동하는 경우

        # 다음턴이 특정 범위 안에 온도가 있어야 한다면
        if onboard[index+1] == 1:
            # 세 가지 케이스 전부 적용
            if t1 < nowtem < t2:
                queue.append([index+1, nowtem + 1, answer + a])
                queue.append([index+1, nowtem - 1, answer + a])
                queue.append([index+1, nowtem, answer + b])
                queue.append([index+1, nowtem, answer + b])
                queue.append([index+1, nowtem + 1, answer])
                queue.append([index+1, nowtem - 1, answer])

            elif nowtem > t2:
                queue.append([index+1, nowtem - 1, answer + a])

            elif nowtem < t1:
                queue.append([index+1, nowtem + 1, answer + a])

            elif nowtem == t2:
                queue.append([index+1, nowtem - 1, answer + a ])
                queue.append([index+1, nowtem, answer + b])

            elif nowtem == t1:
                queue.append([index + 1, nowtem + 1, answer + a])
                queue.append([index+1, nowtem, answer + b])

        elif onboard[index+1] == 0:
            if t1 < nowtem < t2:
                queue.append([index+1, nowtem + 1, answer + a])
                queue.append([index+1, nowtem - 1, answer + a])
                queue.append([index+1, nowtem, answer + b])
                queue.append([index+1, nowtem, answer + b])
                
            elif nowtem > t2:
                queue.append([index+1, nowtem - 1, answer + a])
                queue.append([index + 1, nowtem, answer + b])
             

            elif nowtem < t1:
                queue.append([index+1, nowtem + 1, answer + a])
                queue.append([index + 1, nowtem, answer + b])
             

            elif nowtem == t2:
                queue.append([index+1, nowtem - 1, answer + a ])
                queue.append([index+1, nowtem, answer + b])
          

            elif nowtem == t1:
                queue.append([index + 1, nowtem + 1, answer + a])
                queue.append([index+1, nowtem, answer + b])

            queue.append([index+1, nowtem + 1, answer])
            queue.append([index+1, nowtem - 1, answer])

    return ans

print(solution(28,	18,	26,	10,	8,	[0, 0, 1, 1, 1, 1, 1]))