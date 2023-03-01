def solve(arr):   
    for si in range(1, N+1):
        for sj in range(1, N+1):
            # 4방향
            for di, dj in ((1, 0), (-1, 1), (0, 1), (1, 1)):               
                for mul in range(5):
                    ni, nj = si+di*mul, sj+dj*mul
                    if arr[ni][nj] !='o':
                        break
                else:       # 모두 'o'
                    return 'YES'
    return 'NO'
 
T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = ['.'*(N+2)]+['.'+input()+'.' for _ in range(N)]+['.'*(N+2)]
    ans = solve(arr)
    print(f'#{tc} {ans}')

#################
def is_valid(i, j):
    return 0<=i<N and 0<=j<N
def solve(arr):
    for si in range(N):
        for sj in range(N):
            if arr[si][sj] == 'o':
                for di, dj in ((-1, 1), (0, 1), (1, 1), (1, 0)):
                    for mul in range(5):
                        ni, nj = si + di*mul, sj + dj * mul

                        if not is_valid(ni, nj) or arr[ni][nj] == '.':
                            break
                    else:
                        return 'YES'
    return 'NO'                    
                    
T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = [list(input()) for _ in range(N)]
    
    print(f'#{tc} {solve(arr)}')    