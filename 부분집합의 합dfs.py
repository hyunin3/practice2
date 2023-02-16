def dfs(n, sum, cnt):
    global ans
    if n == N:
        if sum == K and cnt == C:
            ans += 1
        return
    dfs(n + 1, sum + lst[n], cnt + 1)
    dfs(n + 1, sum, cnt)


T = int(input())
for tc in range(1, T + 1):
    C, K = map(int, input().split())
    lst = [n for n in range(1, 13)]
    N = 12
    ans = 0
    dfs(0, 0, 0)
    print(f'#{tc} {ans}')