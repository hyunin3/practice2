T = 10
for _ in range(10):
    tc, V = map(int, input().split())
    stk = []
    lst = list(map(int, input().split()))
    arr = {}
    for i in range(0, V*2, 2):
        s = lst[i]
        e = lst[i+1]
        arr[s] = arr.get(s, []) + [e]

    stk.append(0)
    v = [0] *100  
    while stk:
        a = stk.pop()
        v[a] = 1
        if a in arr.keys():
            for b in arr[a]:
                if not v[b]:
                    stk.append(b) 
        

    print('#{} {}'.format(tc, v[-1]))
                   
