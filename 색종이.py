N = int(input())
arr = [[0] * 100 for _ in range(100)]
for _ in range(N):
    r1, c1 = map(int, input().split())
    for i in range(90-c1, 100-c1):
        for j in range(r1, r1+10):
            arr[i][j] += 1

ans = 0
# for lst in arr:
#     for n in lst:
#         if n >= 1:
#             ans += 1
for i in range(100):
    for j in range(100):
       if arr[i][j] >= 1:
            ans += 1
print(ans)
