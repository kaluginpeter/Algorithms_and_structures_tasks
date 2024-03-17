import datetime

def count_all_mondays(year, lst):
    months: list = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
    days: list = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    count_days: list = [0] * 7
    for month in range(1, 13):
        for day in range(1, 32):
            try:
                date_obj = datetime.date(year, month, day)
                count_days[date_obj.weekday()] += 1
            except ValueError:
                break
    for i in lst:
        if not i:
            continue
        x = datetime.date(year, months.index(i[1]) + 1, int(i[0])).weekday()
        count_days[x] -= 1
    return days[count_days.index(max(count_days))] + ' ' + days[count_days.index(min(count_days))]
n: int = int(input())
year: int = int(input())
lst: list = [input().split() for i in range(n)]
start: str = input()
mondays_count = count_all_mondays(year, lst)
print(mondays_count)
