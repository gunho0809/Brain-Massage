# 2022-07-18
# solved

import sys

a = list(map(int, sys.stdin.readline().split(' ')))
l = list(map(int, sys.stdin.readline().split(' ')))
n = a[0]
m = a[1]  # 나누는 수

hab = [0 for _ in range(n)]  # 부분합
hab[0] = l[0] % m
for i in range(1, n):
    hab[i] = (hab[i - 1] + l[i]) % m
# print(hab)

ms = [0 for _ in range(m)]  # index를 나머지로 가지는 부분합의 갯수
for i in range(n):
    ms[hab[i]] += 1
ms[0] += 1  # 공집합의 부분합
# print(ms)

dab = 0
for i in ms:  # 같은 나머지를 가진 부분합의 쌍의 갯수
    if i > 1:
        dab += i * (i - 1) // 2

print(dab)
