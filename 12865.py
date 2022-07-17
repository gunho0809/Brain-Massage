#2022-07-18
#solved
a = list(map(int, input().split(' ')))
n = a[0]
w = a[1]
obj = []
val = []
nwmap = [[0 for _ in range(n+1)] for _ in range(w+1)]

for _ in range(n):
    l = list(map(int, input().split(' ')))
    obj.append(l[0])
    val.append(l[1])

obj.insert(0,0)
val.insert(0,0)

for nn in range(1,n+1):
    for ww in range(1,w+1):
        if obj[nn] > ww:
            nwmap[ww][nn] = nwmap[ww][nn-1]
        else:
            nwmap[ww][nn] = max(nwmap[ww-obj[nn]][nn-1] + val[nn], nwmap[ww][nn-1])

print(nwmap[w][n])