T = int(input())
for tc in range(1, T + 1):
    arr = list(input() for _ in range(5))
    a=[]
    for lst in arr:
        a.append(len(lst))
    t = max(a)

    ans = ''
    for i in range(t):
        for j in range(5):
            if i < len(arr[j]):
                ans += arr[j][i]

            
    print(f'#{tc} {ans}')        
