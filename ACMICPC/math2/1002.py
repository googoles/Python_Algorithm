
n = int(input())
d = 0
for i in range(n):
    x1,y1,r1,x2,y2,r2 = map(int, input().split())
    dx = x2 - x1
    dy = y2 - y1
    if r1 > r2:
        r1, r2 = r2, r1 # Swap
    d = dx**2 + dy**2
    dist_p = r1 + r2
    dist_m = r2 - r1
    dist_psq = dist_p**2
    dist_msq = dist_m**2
    if dist_psq > d > dist_msq:
        print(2)
    elif d == dist_psq or (d == dist_msq and d != 0):
        print(1)
    elif d < dist_msq or d > dist_psq:
        print(0)
    elif d == 0:
        if (r1 == r2):
            print(-1)
        else:
            print(0)

    # if ((r2 - r1) < d < r1 + r2 and d != 0) or ((r1 - r2) < d < r1 + r2 and d != 0):
    #     print(2)
    # elif d == r1 + r2 or ((d == r2 - r1 or d == r1 - r2) and d != 0):
    #     print(1)
    # elif ((r2-r1 > d) or (r1 - r2 > d)) or (r2 + r1 < d):
    #     print(0)
    # elif d == 0 and r1 == r2:
    #     print(-1)

        # import math
    # d = math.sqrt(((x2-x1)**2)+(y2-y1)**2)