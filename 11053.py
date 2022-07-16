#2022-07-15
#solved

n = input() #수열의 크기
s = input() # 수열

n = int(n)
s = list(map(int, s.split(' ')))
table = [0] * n

for i in range(n):
    max_b = 0
    for j in range(i):
        if s[j] < s[i]:
            max_b = max(max_b, table[j])
    table[i] = max_b + 1

print(max(table))



