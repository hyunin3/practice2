T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    lst = list(map(int, input().split()))
    # mn, mx의 초기값 설정 -> 무조건 갱신되는 값으로
    mn = 1000000
    mx = 0
    for i in range(N - M + 1):
        sum = 0
        for j in range(i, i + M):
            sum = sum + lst[j]
        if mx < sum:
            mx = sum
        if mn > sum:
            mn = sum

        ans = mx - mn

    print(f'#{tc} {ans}')
