def selectionSort(a, N):
    for i in range(N - 1):
        minidx = i
        for j in range(i+1, N):
            if a[minidx] > a[j]:
                minidx = j
        a[i], a[minidx] = a[minidx], a[i]

#################
#1번째부터 k번까지 작은 원소들을 찾아 배열의 앞쪽으로 이동시키고 배열의 k번째 반환

def select(arr, k):
    for i in range(k):
        minidx = i
        for j in range(i+1, len(arr)):
            if arr[minidx] > arr[j]:
                minidx = j

        arr[i], arr[minidx] = arr[minidx], arr[i]

    return arr[k-1]