


def solution(food_times,k):

    eat_time = sorted(food_times)
    l_times = len(food_times)
    count_time = 0
    l_idx = 0
    for idx in range(l_times):
        if idx == 0:
            count_time += eat_time[idx]*(l_times-idx)
        else:
            count_time += (eat_time[idx] - eat_time[idx-1])*(l_times-idx)

        if count_time > k:
            l_idx = idx-1
            break
    if count_time <= k:
        return -1
    lst = []

    for idx in range(l_times-1,-1,-1):
        if food_times[idx] > eat_time[l_idx]:
            lst.append(idx+1)
    if len(lst) != 0:
        return lst[(count_time -k -1)%len(lst)]
    else:
        return k % l_times+1