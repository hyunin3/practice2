def solve(arr):
    cnt = 0
    for lst in arr:
        for i in range(N-M+1):
            if lst[i:i+M ] == lst[i:i+M][::-1]:
                cnt += 1
    return cnt            

    
T =10
for tc in range(1, T + 1):
    N = 8
    M = int(input())
    arr= [list(input()) for _ in range(N)]
    arr_t = list(map(list, zip(*arr)))
    ans = solve(arr) + solve(arr_t)


    print(f'#{tc} {ans}')
