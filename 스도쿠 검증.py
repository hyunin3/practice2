import sys
sys.stdin = open("input.txt", "r")

def test_sudoku(lst):
    test = 0
    # for n in lst:
    #     if sum(n) != 45:
    #         test += 1
    #     else:
    #         pass
    cnt = [0] * 9
    for i in range(N):
        for j in range(N):
            cnt[i] += lst[i][j]
    ans = cnt
    for i in range(N):
        if ans[i] != 45:
            test += 1
        else:
            pass

    cnt = [0] * 9
    for i in range(N):
        for j in range(N):
            cnt[i] += lst[j][i]
    ans = cnt
    for i in range(N):
        if ans[i] != 45:
            test += 1
        else:
            pass

    a = 0
    for i in range(3):
        for j in range(3):
            a += lst[j][i]

    if a != 45:
        test += 1
    else:
        pass

    a = 0
    for i in range(3):
        for j in range(3, 6):
            a += lst[j][i]
    if a != 45:
        test += 1
    else:
        pass
    a = 0
    for i in range(3):
        for j in range(6, 9):
            a += lst[j][i]
    if a != 45:
        test += 1
    else:
        pass
    a = 0
    for i in range(3, 6):
        for j in range(3):
            a += lst[j][i]
    if a != 45:
        test += 1
    else:
        pass
    a = 0
    for i in range(6, 9):
        for j in range(3):
            a += lst[j][i]
    if a != 45:
        test += 1
    else:
        pass
    a = 0
    for i in range(3, 6):
        for j in range(3, 6):
            a += lst[j][i]
    if a != 45:
        test += 1
    else:
        pass
    a = 0
    for i in range(6, 9):
        for j in range(6, 9):
            a += lst[j][i]
    if a != 45:
        test += 1
    else:
        pass
    a = 0
    for i in range(6, 9):
        for j in range(3, 6):
            a += lst[j][i]
    if a != 45:
        test += 1
    else:
        pass
    a = 0
    for i in range(3, 6):
        for j in range(6, 9):
            a += lst[j][i]
    if a != 45:
        test += 1
    else:
        pass

    if test == 0:
        return 1
    else:
        return 0


T = int(input())
for tc in range(1, T + 1):
    N = 9
    lst = [list(map(int, input().split())) for _ in range(N)]

    print(f'#{tc} {test_sudoku(lst)}')

