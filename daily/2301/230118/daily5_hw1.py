# 입력 예시
# 2015
# 8
# 31

# 출력 예시 
#경고 월요일입니다.
#{'년': 2015, '월': 8, '일': 31, '요일': '월요일'}
import calendar
while True:
    year=int(input())
    if year%4==0 and year%10 !=0 or year%400==0:
        print('윤년입니다. 다시 입력하십시오')
    else:
        break

ymd={}
week=['월요일', '화요일', '수요일', '목요일', '금요일', '토요일', '일요일']
month=int(input())
day=int(input())
print(calendar.calendar(year))
dday=week[calendar.weekday(year, month, day)]
if dday=='월요일':
    print(f'경고 {dday}입니다.')
ymd['년']=year
ymd['월']=month
ymd['일']=day
ymd['요일']=dday
print(ymd)
