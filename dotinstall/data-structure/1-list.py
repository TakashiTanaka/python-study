# リスト型のデータを作る

scores = [10, 20, 30, 40]

print(scores)
print(scores[1])

scores[1] = 100  # 値の上書き
scores[100] = 500  # 範囲外のインデックスを指定しているため、エラーとなる

print(scores)
