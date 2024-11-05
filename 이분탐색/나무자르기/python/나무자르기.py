import sys

m,n = map(int, sys.stdin.readline().split())

trees = list(map(int , sys.stdin.readline().split()))
trees.sort()

def binary(s,e):
    while s<=e:

        mid = (s + e) // 2
        ans = 0

        for tree in trees:
            if tree > mid:
                ans += tree - mid

        if ans == n:
            return mid
        
        elif ans < n:
            e = mid - 1

        elif ans > n:
            s = mid + 1

    return s

print(binary(trees[0], trees[-1]))