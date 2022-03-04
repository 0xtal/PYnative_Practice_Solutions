from datetime import datetime, timedelta

given_date = datetime(2020, 2, 25)

new_date = given_date - timedelta(weeks = 1)

print(new_date)