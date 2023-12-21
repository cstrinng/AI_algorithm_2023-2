n, k = input().split()
n = int(n)
k = int(k)
#n, k = map(int, input().split())

a = []
b = []
ans = []

for i in range(n):
    a.append(int(input()))
    
for i in range(k):
    b.append(int(input()))

for j in range(k):
    left = 0
    right = n-1

    while left < right:
        mid = (left + right) // 2
        if a[mid] < b[j]: left = mid + 1
        else: right = mid
    if left == right and a[left] == b[j]:
        ans.append(left)
    else: ans.append(-1)

for i in range(k):
    print(ans[i])