T = int(input())
for test_case in range(1, T + 1):
    lst = list(map(int, input()))
    ans = 0
    # [1] 빈도수 구하기
    cnts = [0] * 10
    for n in lst:
        cnts[n] += 1

    i = 0  # triplet 체크
    while i <= 9:
        if cnts[i] >= 3:  # triplet 인 경우
            ans += 1
            cnts[i] -= 3
        else:
            i += 1

    i = 0  # run 체크
    while i <= 7:
        if cnts[i] >= 1 and cnts[i + 1] >= 1 and cnts[i + 2] >= 1:  # triplet 인 경우
            ans += 1
            cnts[i] -= 1
            cnts[i + 1] -= 1
            cnts[i + 2] -= 1
        else:
            i += 1

    print(f'#{test_case} {ans // 2}')