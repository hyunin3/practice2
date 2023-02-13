T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    arr= [[0]*N for _ in range(N)] #arr로 도장을 찍을 도화지를 만듭니다.

    for _ in range(M): #도장을 찍을 횟수 만큼 범위를 지정합니다.
        r1, c1, r2, c2 = map(int, input().split())

        for i in range(c1, c1+r2):

            for j in range(r1, r1+c2): #arr에 도장을 찍어 1을 더합니다.
                arr[i][j] += 1   #arr[i][j] = 1 하고 해도 됨

    ans = 0  #도장이 찍힌 답을 낼 변수를 만듭니다.
    for lst in arr:
        for n in lst:
            if n >= 1: #도장이 몇번 찍혔든 한번이상 찍히면 찍힌 것으로 세어줍니다.
                ans +=1

    print(f'#{tc} {ans}') #도장이 찍힌 횟수에 상관없이 찍힌 면적만을 구합니다.