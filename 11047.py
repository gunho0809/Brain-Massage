# 2022-07-18
# solved

import sys

a = list(map(int, sys.stdin.readline().split(' ')))
n = a[0]
won = a[1]
coins = []
for _ in range(n):
    coins.append(int(sys.stdin.readline()))
coins.reverse()

coin_count = 0
for c in coins:
    if won < c:
        pass
    else:
        coin_count += won // c
        won = won % c
        if won == 0:
            break

print(coin_count)
