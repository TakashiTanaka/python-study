# 要素をランダムに抽出
import random

names = ["Taro", "Jiro", "Saburo", "Shiro", "Goro"]

# shuffleは破壊的な変更になる
# random.shuffle(names)
# print(names)

# winner = random.choice(names)
# print(winner)

# winners = random.choices(names, k=3)
names = list(set(names))  # 値の重複をしたくない場合、一度setにしてからlistに変換する
winners = random.sample(names, k=3)
print(winners)
