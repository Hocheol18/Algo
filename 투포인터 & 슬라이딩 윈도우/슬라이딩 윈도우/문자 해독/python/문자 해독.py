import sys
from collections import defaultdict

a, b = map(int, sys.stdin.readline().split())
W = sys.stdin.readline().strip()
S = sys.stdin.readline().strip()
answer = 0

target_count = defaultdict(int)
for char in W:
    target_count[char] += 1

window_count = defaultdict(int)
matched = 0

for i in range(len(S)):
    char = S[i]
    if char in target_count:
        window_count[char] += 1

        if window_count[char] == target_count[char]:
            matched += 1

    if i >= len(W):
        left_char = S[i - len(W)]
        if left_char in target_count:

            if window_count[left_char] == target_count[left_char]:
                matched -= 1
            window_count[left_char] -= 1

    if matched == len(target_count):
        answer += 1

print(answer)



# 카운터 쓰는 방식

import sys
from collections import Counter

a, b = map(int, sys.stdin.readline().split())
W = sys.stdin.readline().strip()
S = sys.stdin.readline().strip()

w_counter = Counter(W)

window_counter = Counter(S[:a])

match_count = sum(1 for c in w_counter if window_counter[c] == w_counter[c])

answer = 1 if match_count == len(w_counter) else 0

for i in range(a, len(S)):
    left_char = S[i - a]
    if left_char in w_counter:
        if window_counter[left_char] == w_counter[left_char]:
            match_count -= 1
        window_counter[left_char] -= 1
        if window_counter[left_char] == w_counter[left_char]:
            match_count += 1

    right_char = S[i]
    if right_char in w_counter:
        if window_counter[right_char] == w_counter[right_char]:
            match_count -= 1
        window_counter[right_char] += 1
        if window_counter[right_char] == w_counter[right_char]:
            match_count += 1

    if match_count == len(w_counter):
        answer += 1

print(answer)