T = 10
for tc in range(1, T + 1):
    _ = int(input())
    st1 = input()
    st2 = input()
    N, M = len(st2), len(st1)
    ans = 0

    for i in range(0, N - M + 1):
        for j in range(M):
            if st1[j] != st2[i+j]:
                break
        else:
            ans += 1

    print(f'#{tc} {ans}')
