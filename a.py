T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())  
    a= list(map(int, input().split()))
    b= list(map(int, input().split()))
    if N > M:
        N, M = M, N
        a, b = b, a
    ans = -10000
    
   
    for i in range(M - N + 1):
        sum = 0
        for j in range(N):
            sum = sum + a[j] * b[i+j]
        if ans < sum:
            ans = sum

    print(f'#{tc}', ans)            


