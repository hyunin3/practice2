T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    lst = [2,3,5,7,11]
    cnt = [0]*5
    for i in range(len(lst)):
        while N % lst[i] == 0:
            N = N / lst[i]
            cnt[i] += 1

            
    print(f'#{tc}', *cnt)            