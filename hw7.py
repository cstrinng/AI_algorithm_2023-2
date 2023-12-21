def insertionSort(a:list, n:int):
    for i in range(n):
        tmp = a[i]
        j = i - 1
        while j >= 0:
            if a[j] <= tmp: break
            a[j+1] = a[j]
            j -= 1
        a[j+1] = tmp
        

n = int(input())
a = []
for i in range(n):
    a.append(int(input()))
    
insertionSort(a, n)

for i in range(n):
    print(a[i])