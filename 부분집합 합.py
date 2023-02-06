T = int(input())
for tc in range(1, T + 1):
    lst = list(map(int, input().split()))
    N = len(lst)
    ans = 0  # 초기값 false

    # 공집합을 제외한 모든 조합을 비트로 표시
    for bit in range(1, 1 << N):
        sum = 0
        # bit 0의 자리부터 bit(n-1)까지 한 자리씩 flag 체크
        for j in range(N):
            if bit & (1 << j):  # 해당 비트가 0이 아니면 포함!
                sum += lst[j]
        if sum == 0:
            ans = 1
            break  # 이미 찾았다면 더 이상 찾을 필요 없음

    print(f'#{tc} {ans}')