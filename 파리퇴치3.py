def is_valid(i, j):
    return 0<=i<N and 0<=j<N

T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    ans1 = 0
    for si in range(N):
        for sj in range(N):
            sm1 = arr[si][sj]
            for di, dj in ((-1, 0), (1, 0), (0, -1), (0, 1)):
                for mul in range(1, M):
                    ni, nj = si + mul*di, sj + mul*dj
                    if is_valid(ni, nj):
                        sm1 += arr[ni][nj]
                if ans1 < sm1:
                    ans1 = sm1

    ans2 = 0
    for si in range(N):
        for sj in range(N):
            sm2 = arr[si][sj]
            for di, dj in ((-1, -1), (1, 1), (-1, 1), (1, -1)):
                for mul in range(1, M):
                    ni, nj = si + mul*di, sj + mul*dj
                    if is_valid(ni, nj):
                        sm2 += arr[ni][nj]
                if ans2 < sm2:
                    ans2 = sm2

    ans = max(ans1, ans2)

    print(f'#{tc} {ans}')
