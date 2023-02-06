T = int(input())
for tc in range(1, T + 1):
    N = int(input())  #입력 사각형 개수
    ans = 0
    arr = [[0]*10 for _ in range(10)]
    
    for _ in range(N):
        R1, C1, R2, C2, color = map(int, input().split())
        for i in range(R1, R2 + 1):
            for j in range(C1, C2 + 1):
                arr[i][j] += color
                
    for i in range(10):
        for j in range(10):
            if arr[i][j] == 3:
                ans += 1
    print(f'#{tc} {ans}')                        