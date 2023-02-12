T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    lst = list(map(int, input().split()))
 
    for i in range(10):
        idx = i
        for j in range(i + 1, N):
            if i % 2 != 0:
                if lst[idx] > lst[j]:
                    idx = j
            else:
                if lst[idx] < lst[j]:
                    idx = j
        lst[idx], lst[i] = lst[i], lst[idx]

    print(f'#{tc}', *lst[:10])                       