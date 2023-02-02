T = int(input())
for test_case in range(1, T + 1):
    K, N, M = map(int, input().split())
    lst = [0]+ list(map(int, input().split())) + [N]
 
    ans = s = 0
    for i in range(1, len(lst)):
        # 정류장 사이가 K 이상인 경우 ==> 도달 불가능!
        if lst[i]-lst[i-1]>K:
            ans=0
            break
 
        # 기준점(start)에서 현재 위치가 이동 불가능한 경우==>충전
        if lst[i]-lst[s] > K:
            ans+=1
            s=i-1
 
    print(f'#{test_case} {ans}')