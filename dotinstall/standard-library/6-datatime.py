# 日時を扱うdatetime

import datetime

# 現在時刻
now = datetime.datetime.now()
print(now)

# 特定の日付情報
birthday = datetime.datetime(year=2000, month=4, day=20)
print(birthday)

# 特定の日付情報を文字列から生成する
birthday = datetime.datetime.strptime("2000-04-11", "%Y-%m-%d")
print(birthday)
