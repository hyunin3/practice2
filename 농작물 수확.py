T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input())) for _ in range(N)]
    mid = N//2
    s = e = mid
    sm = 0
    for i in range(N):
        for j in range(s, e + 1):
            sm += arr[i][j]
        if i < mid:
            s -= 1
            e += 1
        else:
            s += 1        
            e -= 1
    print(f'#{tc} {sm}')        