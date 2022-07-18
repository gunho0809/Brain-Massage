#2022-07-18
#solved
import sys
a = list(map(int, sys.stdin.readline().split(' ')))
n = a[0]
l = list(map(int, sys.stdin.readline().split(' ')))
ij = []
for _ in range(a[1]):
    ij.append(list(map(int, sys.stdin.readline().split(' '))))
nhab = [0 for _ in range(n+1)] #누적합
nhab[0] = l[0]
for i in range(1,n):
    nhab[i] = nhab[i-1] + l[i]
for i in ij:
    print(nhab[i[1]-1] - nhab[i[0]-2])