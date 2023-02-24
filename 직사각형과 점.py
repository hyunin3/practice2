T = int(input())
for tc in range(1, T + 1):
    x1, y1, x2, y2 = map(int, input().split())
    N = int(input())
    a = b = c = 0
    for _ in range(N):
        x, y = map(int, input().split())
        if x1 < x < x2 and y1 < y < y2:
            a += 1
        elif x < x1 or y < y1 or x > x2 or y > y2:
            c += 1
        else:
            b += 1

    print(f'#{tc} {a} {b} {c}')