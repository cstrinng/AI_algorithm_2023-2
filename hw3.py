n, m = map(int, input().split())

a = []
b = []

for i in range(n):
    a.append(input())
    
for j in range(m):
    b.append(input())
    

def computeFailNaive(pat : str) -> list:
    f = [0 for i in range(m)]
    for i in range(m):
        f[i] = 0
        for j in range(i, 0, -1):
            matched = True
            for k in range(j):
                if pat[k] != pat[i - (j - 1) + k]:
                    matched = False
                    break
            if matched:
                f[i] = j
                break
    return f

f = computeFailNaive(b)

def kmpMatch(a : str, b : str, f : list, n : int, m : int) -> int:
    posT, posP= 0, 0
    while (posT < n) and (posP < m):
        if a[posT] == b[posP]:
            posT += 1
            posP += 1
        else:
            if posP == 0:
                posT += 1
            else:
                posP = f[posP - 1]
                
    if posP < m:
        return -1
    else:
        return posT - m

            

ans = kmpMatch(a, b, f, n, m)

print(ans)