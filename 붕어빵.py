T = int(input())
for tc in range(1, T + 1):
    N, M, K = map(int, input().split())
    lst = list(map(int, input().split()))
    lst.sort()  #정렬하여 첫 손님과 마지막 손님을 시간으로 이용
   
    for i in range(N):
        if (lst[i] // M) * K < i + 1:
            ans = 'Impossible'
            break
    else:
        ans = 'Possible'

    print(f'#{tc} {ans}')

