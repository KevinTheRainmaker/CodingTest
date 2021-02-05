def solution(a, b):
    week = ['THU','FRI','SAT','SUN','MON','TUE','WED']
    month = [0,31,29,31,30,31,30,31,31,30,31,30,31]
    day = 1
    for i in range(a):
        day += month[i]
    day += (b-1)
    answer = week[day%7]
    return answer