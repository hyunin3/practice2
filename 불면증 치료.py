T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    num = str(N)
    cnt = [0] * 10
    while True:
        for ch in num:
            cnt[int(ch)] = 1
        if not 0 in cnt:
            break
        num = str(int(num) + N)
    print(f'#{tc} {num}')        

    
