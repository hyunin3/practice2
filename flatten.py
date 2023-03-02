def max_min(lst):
    mn = mx =0
    for i in range(1, len(lst)):
        if lst[mn] > lst[i]:
            mn = i
        if lst[mx] < lst[i]:
            mx = i
    return mn, mx

T = 10
for tc in range(1, T + 1):
    N = int(input())
    lst = list(map(int, input().split()))
    for _ in range(N):
        mn, mx = max_min(lst)
        lst[mn] += 1
        lst[mx] -= 1

    mn, mx = max_min(lst)
    ans = lst[mx]-lst[mn]
    print(f'#{tc} {ans}')
