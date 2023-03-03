import sys
sys.stdin = open("input.txt", "r")
N = int(input())
arr = [[0] * 1001 for _ in range(1001)]
for t in range(1, N+1):
    r, c, w, h = map(int, input().split())
    for i in range(r, r+w):
        for j in range(c, c+h):
            arr[i][j] = t

for k in range(1, N+1):
    ans = 0
    for lst in arr:
        for n in lst:
            if n == k:
                ans += 1
    print(ans)  



