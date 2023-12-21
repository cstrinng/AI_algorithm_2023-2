def doMergeSort(a:list, left:int, right:int, aux:list):
    if left >= right : return
    mid = (left+right) // 2
    doMergeSort(a, left, mid, aux)
    doMergeSort(a, mid + 1, right, aux)

    i, j, k = left, mid + 1, left
    while i <= mid and j <= right :
        if a[i] <= a[j]: aux[k], k, i = a[i], k+1, i+1
        else : aux[k], k, j = a[j], k+1, j+1

    while i <= mid : aux[k], k, i = a[i], k+1, i+1
    while j <= right : aux[k], k, j = a[j], k+1, j+1
    
    for i in range(left, right+1) : a[i] = aux[i]


n = int(input())
a = [0 for _ in range(n)]
aux = [0 for _ in range(n)]
for i in range(n):
    a[i] = int(input())
    
doMergeSort(a, 0, n-1, aux)

for i in range(n):
    print(a[i])