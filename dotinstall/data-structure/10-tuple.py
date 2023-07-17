# タプル型

# in, len(), index(), count() →使える
# append(), insert(), pop() → 使えない

# リスト型と似ているが、タプル型は要素やその順序等を変更できない（タプルをリスト型に変換すれば変更できる）

# tokyo = ("JPY", 36, 140)
tokyo = "JPY", 36, 140

print(tokyo)
print(tokyo[0])

tokyo = list(tokyo)  # タプルをリスト化
tokyo = tuple(tokyo)  # リストをタプル化
