T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = list(map(int, input().split()))
    for i in range(N):
        for j in range(N-1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    

    print(f'#{tc}',*arr)        
    
    
################

lst=[2,3,5,1,2,7,4,8,9,5,0,1]
N = len(lst)
def bubblesort(lst, N):
    for i in range(N):
        for j in range(N-1):
            if lst[j]>lst[j+1]:
                lst[j], lst[j + 1] = lst[j + 1], lst[j]
    return lst
print(bubblesort(lst, N))    