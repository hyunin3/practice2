def solve(arr):
    ans = 0
    for lst in arr:
        cnt = 0
        for i in lst:
            if i == 1:
                cnt += 1
            elif i == 0:
                if ans < cnt:
                    ans = cnt
                cnt = 0
    return ans                    

T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) + [0] for _ in range(N)] + [[0] * (N + 1)]
    arr_t = list(map(list, zip(*arr)))
    if solve(arr) < solve(arr_t):
        a= solve(arr_t)
    else:
        a = solve(arr)    
    print(f'#{tc} {a}')