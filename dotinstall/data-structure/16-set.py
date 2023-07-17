# 集合

# 重複する要素は無視される・順序が保証されない
members = {"Taro", "Jiro", "Saburo", "Taro"}

print(members)

members.add("Shiro")
members.remove("Taro")

print(members)

print(len(members))
print("Jiro" in members)

# frozenset関数を使ってmembersを変更できないデータ型に変換する
frozen_members = frozenset(members)
frozen_members.add("Goro")

print(members)
