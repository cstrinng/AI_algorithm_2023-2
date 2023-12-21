
n = int(input())

numList = list()
ans = list()

i = 1
while True:
    line = input()
    numList = line.split()
    if numList[1] == 'plus':
        ans.append(int(numList[0]) + int(numList[2]))
    elif numList[1] == 'times':
        ans.append(int(numList[0]) * int(numList[2]))

    if i == n: break
    i += 1
    
j = 0
for j in range (n):
    print(ans[j])