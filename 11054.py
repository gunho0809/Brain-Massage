#2022-07-17
#solved
n = int(input())
l = list(map(int, input().split(' ')))

lm = 0 #left_max
rm = 0 #right_max
tm = 0 #total_max
lt = [1 for _ in range(n)]
rt = [1 for _ in range(n)]

for i in range(n):
    lm = 0
    for e in range(i):
        if l[i] > l[e]:
            lm = max(lt[e], lm)
    lt[i] = lm + 1

l.reverse()

for i in range(n):
    rm = 0
    for e in range(i):
        if l[i] > l[e]:
            rm = max(rt[e], rm)
    rt[i] = rm + 1

for i in range(n):
    tm = max(tm, lt[i] + rt[n-1-i] - 1)

print(tm)