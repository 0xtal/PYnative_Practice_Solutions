from datetime import datetime, timedelta

# 2020-03-22 10:00:00
given_date = datetime(2020, 3, 22, 10, 0, 0)

new_date = given_date + timedelta(hours = 12, weeks = 1)
print(new_date)