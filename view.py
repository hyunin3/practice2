T = 10
for tc in range(1, T + 1):
    N = int(input())
    lst = list(map(int, input().split()))
    cnt = 0
    for i in range(2, N-2):
        if lst[i] <= max(lst[i-2], lst[i-1], lst[i+1], lst[i+2]):
            continue
        else:
            cnt += lst[i] - max(lst[i-2], lst[i-1], lst[i+1], lst[i+2])


    print(f'#{tc} {cnt}')
###########################
T = 10
for tc in range(1, T + 1):
    N = int(input())
    lst = list(map(int, input().split()))
    cnt = 0
    for i in range(2, N-2):
        if lst[i] > max(lst[i-2], lst[i-1], lst[i+1], lst[i+2]):
            cnt += lst[i] - max(lst[i-2], lst[i-1], lst[i+1], lst[i+2])
    print(f'#{tc} {cnt}')
    #이렇게 해도 되는데 시간은 더 오래 걸림    