di = [-1, 0, 1, 0, -1, 1, 1, -1]
dj = [0, 1, 0, -1, 1, -1, 1, -1]
T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    arr = [[10] * (M + 2)] + [[10] + list(map(int, input().split())) + [10] for _ in range(N)] + [[10] * (M + 2)]
    ans = 0
    for si in range(1, N+1):
        for sj in range(1, M+1):
            cnt = 0
            for mul in range(8):
                ni, nj = si+di[mul], sj+dj[mul]
                if arr[si][sj] > arr[ni][nj]:
                    cnt += 1
            if cnt >= 4:
                ans += 1

    print(f'#{tc} {ans}')