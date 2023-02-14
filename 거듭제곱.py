def f(N, M):
    if M == 1:
        return N
    else:
        return f(N, M-1) * N


T = 10
for tc in range(1, T + 1):
    _ = int(input())
    N, M = map(int, input().split())
    ans = f(N, M)
    print(f'#{tc} {ans}')