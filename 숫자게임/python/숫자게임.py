def solution(A, B):
    answer = 0
    B_dic = {}
    B.sort()
    
    for i in B:
        if i not in B_dic:
            B_dic[i] = 1
        else:
            B_dic[i] += 1
    
    for i in A:
        flag = True
        first = 0
        for j, values in B_dic.items():
            if values > 0 and flag:
                B_dic[j] -= 1
                flag = False
                first = j
            if j > i and values > 0:
                B_dic[j] -= 1
                answer += 1
                B_dic[first] += 1
                break
        
    return answer

# 1차 실패

# 그리디
def solution(A, B):
    answer = 0
    B.sort()
    A.sort()
    j = -1
    for i in range(len(B)):
        while True:
            if j + 1 == len(B):
                break
            j += 1
            if A[i] < B[j]:
                answer += 1
                break
                
    return answer


# 이분탐색 풀이
from bisect import bisect_right

def solution(A, B):
    answer = 0
    A.sort()
    B.sort()
    
    # B에서 사용할 인덱스 포인터
    used_index = 0
    
    for a in A:
        # B에서 A[i]보다 큰 값의 첫 번째 인덱스를 이분 탐색으로 찾음
        idx = bisect_right(B, a, used_index)
        
        # idx가 B의 범위 내에 있으면 B[idx]를 사용
        if idx < len(B):
            answer += 1
            used_index = idx + 1  # 사용한 B[j] 이후 인덱스로 이동
    
    return answer