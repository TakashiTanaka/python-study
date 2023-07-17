# 文字列とリスト型の相互変換

# 文字列を特定の区切り文字で連結してリスト型に変換
# birthday = "2011-11-27"
# print(birthday.split("-"))

# リスト型を特定の文字列で結合して文字型に変換
# birthday = ["2011", "11", "27"]
# print("-".join(birthday))

# 数値を一度リスト内包表記で一旦文字列の要素にしてから文字列に変換
birthday = [2011, 11, 27]
print("-".join([str(n) for n in birthday]))
