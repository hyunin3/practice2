lst = []
for _ in range(9):
    n = int(input())
    lst.append(n)
alst = []
N = 9

for i in range(0, N-6):
    for j in range(i+1, N-5):
        for k in range(j+1, N-4):
            for l in range(k+1, N-3):
                for m in range(l+1, N-2):
                    for n in range(m+1, N-1):
                        for o in range(n+1, N):
                            sm = lst[i]+lst[j]+lst[k]+lst[l]+lst[m]+lst[n]+lst[o]
                            if sm == 100:
                                alst.append(lst[i])
                                alst.append(lst[j])
                                alst.append(lst[k])
                                alst.append(lst[l])
                                alst.append(lst[m])
                                alst.append(lst[n])
                                alst.append(lst[o])
                            else:
                                continue

alst.sort()
for num in alst:
    print(num)
