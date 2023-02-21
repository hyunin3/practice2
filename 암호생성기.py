T = 10
for tc in range(1, T + 1):
    _ = input()
    q = list(map(int, input().split()))
    n = 1
    while True:
        t = q.pop(0) - n
        if t < 0:
            t = 0
        q.append(t)
        if t == 0:
            break
        n = n % 5 + 1
    print(f'#{tc}', *q)        