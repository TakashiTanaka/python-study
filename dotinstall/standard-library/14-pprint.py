# pprintモジュール

# import pprint
from pprint import pprint

scores = [
    {"name": "Taro", "math": 70, "english": 82},
    {"name": "Jiro", "math": 67, "english": 61},
    {"name": "Saburo", "math": 81, "english": 58},
]

# 普通のprintだと若干読みづらい
# print(scores)

# pprintメソッドを使うといい感じに出力してくれる
# pprint.pprint(scores)

# 予めpprintモジュールからpprintメソッドだけを取り込んでおけば短く書ける
pprint(scores)
