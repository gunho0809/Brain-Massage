#2022-07-17
#solved

ls = []
while(1):
    l = list(map(int, input().split(' ')))
    if l[0] == -1 and l[1] == -1 and l[2] == -1:
        break
    else:
        ls.append(l)
for l in ls:
    if (l[0] <= 0 or l[1] <= 0 or l[2] <= 0):
        print('w(%d, %d, %d) = %d' % (l[0], l[1], l[2], 1))
    elif (l[0] > 20 or l[1] > 20 or l[2] > 20):
        a = 20
        b = 20
        c = 20
        print('w(%d, %d, %d) = %d'%(l[0],l[1],l[2],1048576))
    else:
        a = max(l[0],0)
        b = max(l[1],0)
        c = max(l[2],0)
        tb = [[[0 for _ in range(c+1)] for _ in range(b+1)] for _ in range(a+1)]
        for i in range(a+1):
            for j in range(b+1):
                for k in range(c+1):
                    if (i==0 or j==0 or k==0):
                        tb[i][j][k] = 1
                    elif (i < j and j < k):
                        tb[i][j][k] = tb[i][j][k-1] + tb[i][j-1][k-1] - tb[i][j-1][k]
                    else:
                        tb[i][j][k] = tb[i-1][j][k] + tb[i-1][j-1][k] + tb[i-1][j][k-1] - tb[i-1][j-1][k-1]
        print('w(%d, %d, %d) = %d'%(l[0],l[1],l[2],tb[a][b][c]))