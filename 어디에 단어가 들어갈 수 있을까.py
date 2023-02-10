def count(arr):
    ans = 0
    for lst in arr:
        cnt = 0
        for n in lst:
            if n == 1:
                cnt += 1
            elif n == 0:
                if cnt == K:
                    ans += 1
                cnt = 0
    return ans

T = int(input())
for tc in range(1, T+1):
    N, K = map(int, input().split())
    arr = [list(map(int, input().split())) + [0] for _ in range(N)] + [[0]*(N+1)]
    arr_t = list(map(list, zip(*arr))) #전치행렬

    print(f'#{tc} {count(arr) + count(arr_t)}')