def is_valid(i, j):
    return 0<=i<N and 0<=j<M
 
T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    ans = 0
    for si in range(N):
        for sj in range(M):
            sm = arr[si][sj]
            t = arr[si][sj]
            for di, dj in ((-1, 0), (1, 0), (0, 1), (0, -1)):
                for mul in range(1, t+1):
                    ni, nj = si + di*mul, sj + dj*mul
                    if is_valid(ni, nj):
                        sm += arr[ni][nj]
 
                if ans < sm:
                    ans = sm
    print(f'#{tc} {ans}')                        
 