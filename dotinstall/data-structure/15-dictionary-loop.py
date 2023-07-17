# 辞書型とループを組み合わせる

scores = {"math": 62, "english": 91, "physics": 84}

# キーのみ取得
for key in scores.keys():
    print(key)

# valueのみ取得
for value in scores.values():
    print(value)

# タプルで取得
# for item in scores.items():
#     # print(item)
#     key, value = item
#     print(f"{key:8} {value:3}")

# 上の記述をもっと簡略化
for key, value in scores.items():
    print(f"{key:8} {value:3}")
