# シーケンスの理解

# シーケンスとは、インデックスを使ってアクセスできる型の事。
# リスト、タプル、文字型など

scores = [10, 20, 30, 20, 40]
tokyo = ("JPY", 36, 140)
name = "Taro Yamada"

print(name[0])
print(name[:4])

# 文字列に特化した、破壊的なメソッドが色々とある
replaced_string = name.replace("Taro", "Jiro")
upper_string = name.upper()
print(replaced_string)
print(upper_string)
