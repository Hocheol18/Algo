import sys

n, x = map(int, sys.stdin.readline().split())

data = list(map(int, sys.stdin.readline().split()))

answer = sum(data[i] for i in range(0, x))

max_sum, max_sum_count = answer, 1
for i in range(0, n-x):
    answer -= data[i]
    answer += data[i + x]

    if answer > max_sum:
        max_sum = answer
        max_sum_count = 1
    elif answer == max_sum:
        max_sum_count += 1

if max_sum == 0:
    print("SAD")
else:
    print(max_sum)
    print(max_sum_count)