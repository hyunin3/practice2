def f(N):
    for i in range(N - 1):
        for j in range(i + 1):
            if lst[j] > lst[j + 1]:
                lst[j], lst[j + 1] = lst[j + 1], lst[j]
                print(*lst)
                if lst != [1, 2, 3, 4, 5]:
                    f(N)
            else:
                pass

lst = list(map(int, input().split()))
N = len(lst)
f(N)