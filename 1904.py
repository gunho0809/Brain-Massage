#2022-07-16
#solved

n = int(input())
if n == 1:
    print(1)
elif n == 2:
    print(2)
else:
    n1 = 1
    n2 = 2
    for i in range(n-2):
        n3 = (n1 + n2)%15746
        n1 = n2
        n2 = n3
    print(n3%15746)