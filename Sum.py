T = 10
for tc in range(1, T + 1):
    _ = int(input())
    N = 100
    arr = [list(map(int, input().split())) for _ in range(N)]
    ans = 0
    for i in range(N):
        sum1 = 0
        sum2 = 0
        for j in range(N):
            sum1 += arr[i][j]
            sum2 += arr[j][i]
        if ans < sum1:
            ans = sum1
        if ans < sum2:
            ans = sum2
    sum3 = 0
    sum4 = 0
    for i in range(N):
        sum3 += arr[i][i]
        sum4 += arr[i][N -1 -i]
    if ans < sum3:
        ans = sum3
    if ans < sum4:
        ans = sum4

    print(f'#{tc} {ans}')