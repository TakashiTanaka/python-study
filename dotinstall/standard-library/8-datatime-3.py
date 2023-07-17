# 日時の計算

import datetime

day1 = datetime.datetime(year=2000, month=4, day=11)
day2 = datetime.datetime(year=2001, month=1, day=1)

# 引き算できる
diff = day2 - day1  # timedelta型

# timedelta型の値を数値型に変換
# diff_seconds = diff.total_seconds()
# print(diff_seconds)

# 日数に計算し直す
# diff_days = diff.total_seconds() / 60 / 60 / 24
# print(diff_days)

# 特定の日付から指定した値を足して表現
delta = datetime.timedelta(days=3, hours=5)
day3 = day1 + delta
print(day3)
