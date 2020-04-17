def search(li, begin, end, target):
    if begin>end:
        return -1
    elif target == li[begin]:
        return begin
    else:
        return search(li,begin+1, end, target)

li = [1,6,10,7,2,5]
target = 10
search(li,0,5,10)