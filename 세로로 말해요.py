T = int(input())
for tc in range(1, T + 1):
    arr = [list(input()) for _ in range(5)]
    a = []
    for lst in arr:
        a.append(len(lst))
    t = max(a)

    ans = ''
    for j in range(t):
        for i in range(5):
            if j < len(arr[i]):
                ans += arr[i][j]

    print(f'#{tc} {ans}')