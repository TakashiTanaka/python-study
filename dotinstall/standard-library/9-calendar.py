# calendarモジュール

import calendar

# 日曜日始まりに変更
# calendar.setfirstweekday(6)
calendar.setfirstweekday(calendar.SUNDAY)

# 文字型で取得
cal_str = calendar.month(2022, 8)
print(cal_str)  # デフォルトでは月曜日始まり

# リスト型で取得
cal_data = calendar.monthcalendar(2022, 8)
print(cal_data)

# うるう年の判定
print(calendar.isleap(2000))
print(calendar.isleap(2001))
