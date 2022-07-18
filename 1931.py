# 2022-07-18
# solved

import sys

n = int(sys.stdin.readline())
meets = []
for _ in range(n):
    meets.append(list(map(int, sys.stdin.readline().split(' '))))

# 회의를 종료시간으로 정렬
meets.sort(key=lambda x: (x[1], x[0]))

s_time = meets[0][0]  # 시작시각
e_time = meets[0][1]  # 종료시각
count_meet = 1
del meets[0]

for meet in meets:
    if meet[0] >= e_time:
        s_time = meet[0]
        e_time = meet[1]
        count_meet += 1

print(count_meet)