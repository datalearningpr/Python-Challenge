

# test about datetime and calendar library

import datetime, calendar

dates = []

for year in range(1006, 1997, 10):
    day = datetime.date(year, 1, 26)
    if calendar.isleap(year) and day.isoweekday() == 1:
        dates.append(day)

print(dates[-2])


