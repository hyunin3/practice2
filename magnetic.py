T = 10
for tc in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    arr_t = list(map(list, zip(*arr)))
    ans = 0
    for lst in arr_t:
        prev = 0
        for i in lst:
            if i:
                if i == 2 and prev == 1:
                    ans += 1
                prev = i
 
    print(f'#{tc} {ans}')