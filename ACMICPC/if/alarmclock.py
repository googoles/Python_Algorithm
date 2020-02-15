h,m = list(map(int, input().split()))

if m >= 45:
    print(h,m-45)
else:
    if h == 0:
        print(23,15+m) # 59~16까지 변화
    else:
        print(h-1,15+m)