T = int(input())
for tc in range(1, T + 1):
    st = input()
    cnt = 0
    sum = 0
    for chr in st:
        if chr == 'O':
            cnt += 1
            sum += cnt
        else:
            cnt = 0

    print(sum)