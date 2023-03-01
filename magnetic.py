T = 1
for tc in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    ans = 0
    for j in range(N):
        cnt = 0
        for i in range(N):
            if arr[i][j] == 1:
                cnt = 1
            elif arr[i][j] == 2:
                if cnt:
                    ans += 1
                    cnt = 0                          
                  
    print(f'#{tc} {ans}')                         