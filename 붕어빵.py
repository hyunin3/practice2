T = int(input())
for tc in range(1, T + 1):
    N, M, K = map(int, input().split())
    lst = list(map(int, input().split()))
    lst.sort()  #정렬하여 첫 손님과 마지막 손님을 시간으로 이용
    a = K/M  #초당 붕어빵 만드는 개수
    if lst[-1] * a >= len(lst) and lst[0] >= M: #총시간(마지막손님)*초당 제작 개수 >= 손님수 , 첫 손님은 첫 제작 이후 와야한다
        ans = 'Possible'
    else:
        ans = 'Impossible'
    # for i in range(N):
    #     if (lst[i] // M) * K < i + 1:
    #         ans = 'Impossible'
    #         break
    # else:
    #     ans = 'Possible'


    print(f'#{tc} {ans}')

