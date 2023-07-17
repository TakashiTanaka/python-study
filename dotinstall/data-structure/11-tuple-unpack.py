# タプル型のアンパック

tokyo = "JPY", 36, 240

# アンパック（分割代入的なやつ？）
currency, lat, long = tokyo

print(currency, lat, long)

# Pythonでは使用しない値を_で表記する慣習がある
_, lat, long = tokyo

# 変数名の前に*をつけると代入されていない値がリスト型として代入される
currency, *location = tokyo
print(currency, location)

# currencyだけ使いたい、という場合は下記のようにかける
currency, *_ = tokyo
