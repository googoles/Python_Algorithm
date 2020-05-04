

def solution(n,t,m,timetable):
    answer = ''

    timetable = [int(time[:2])*60 + int(time[3:5]) for time in timetable]

    timetable.sort()

    for i in range(n):

        last_time = 540 + (n-1) * t

        if len(timetable) < m:
            return '%02d:%02d' % (last_time // 60, last_time % 60)
        if i == n-1:
            if timetable[0] > last_time:
                return '%02d:%02d' % (last_time // 60, last_time % 60)
            time = timetable[m-1] -1
            return '%02d:%02d' % (time // 60, time % 60)
        for  j in range(m-1,-1,-1):
            bus_arrive = 540 + i * t
            if timetable[j] <= bus_arrive:
                del timetable[j]