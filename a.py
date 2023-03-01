T = 1
for tc in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    cnt = 0
    for sj in range(N):
        for si in range(N):
            if arr[si][sj] == 1:
                for j in range(sj, N):
                    for i in range(si, N):
                         if arr[i][j] == 2:
                             cnt += N-i
    print(f'#{tc} {cnt}')                         

               


    
        
     
                          
     
           