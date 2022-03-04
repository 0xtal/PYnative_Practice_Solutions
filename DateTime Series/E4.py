from datetime import datetime

given_date = datetime(2020, 2, 25)

format_date = given_date.strftime('%A %d %B %Y')
print(format_date)