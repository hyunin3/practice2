T = int(input())
for tc in range(1, T + 1):
    N, D = map(int, input().split())
    lst =list(map(int, input().split()))
    cnt = 0
    for i in range(N):
        if lst[i] == D:
            cnt = i
        elif cnt == 0:
             cnt = -1

    print(f'#{tc}', cnt+1)