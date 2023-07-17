# 日時を扱うdatetime

import datetime

# datetime型
birthday = datetime.datetime(year=2000, month=4, day=20)
print(birthday)

print(birthday.year)
print(birthday.month)
print(birthday.day)
print(birthday.hour)
print(birthday.minute)
print(birthday.second)
print(birthday.microsecond)
print(birthday.weekday())  # Mon:0, Tue:1, ... Sun:6

# datetime型をstring型に変換
birthday_formatted = birthday.strftime("%B %d %A %Y")
print(birthday_formatted)
