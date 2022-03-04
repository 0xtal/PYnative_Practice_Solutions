from datetime import date, datetime

date_string = "Feb 25 2020 4:20PM"

dt_obj = datetime.strptime(date_string, "%b %d %Y %H:%M%p")
print(dt_obj)