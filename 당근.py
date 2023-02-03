T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    lst = list(map(int, input().split()))
    ans = 1 #이 문제에선 ans, cnt의 최솟값이 1
    cnt = 1
    for i in range(N-1): #마지막 칸에선 실행 안함
        if lst[i] + 1 == lst[i+1]:
            cnt += 1
            if ans < cnt:
                ans = cnt
        else:
            cnt = 1

    print(f'#{tc}', ans)