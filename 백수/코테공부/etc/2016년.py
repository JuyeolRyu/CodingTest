import datetime
def solution(a, b):
    weekday = ['MON','TUE','WED','THU','FRI','SAT','SUN']
    answer = weekday[datetime.date(2016,a,b).weekday()]
    return answer