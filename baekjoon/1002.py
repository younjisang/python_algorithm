import math

t = input()
t = int(t)

for _ in range(t):
    x1, y1, r1, x2, y2, r2 = map(int, input().split())
    D = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

    if r1 == r2 and D == 0:
        print(-1)
    elif D == r1 + r2 or D == abs(r1-r2):
        print(1)
    elif r1 > D + r2 or r2 > D + r1 or D > r1 + r2:
        print(0)
    elif D < r1 + r2 and abs(r1-r2) < D: print(2)
