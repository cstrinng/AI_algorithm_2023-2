def findA(n, i, j):
    k = 2**(n-1)
    if n == 0:
        return 0
    elif (i <= k and j > k) or (i > k and j <= k):
        return n
    elif (i <= k and j <= k):
        return findA(n-1, i, j)
    elif (i > k and j > k):
        return findA(n-1, i-k, j-k)


k = int(input())
for i in range(k):
    n, i, j = map(int, input().split())
    print(findA(n, i, j))



'''

print(findA(1, 1, 1))
print(findA(1, 1, 2))
print(findA(1, 2, 1))
print(findA(1, 2, 2))
print(findA(2, 1, 3))
print(findA(2, 1, 4))
print(findA(2, 3, 3))
print(findA(2, 3, 4))

print('.')

for i in range (1, 9):
    for j in range(1, 9):
        print(findA(3, i, j))    

'''