# 乱数を生成
# import random # randomモジュールを読み込み

# import random as r  # ライブラリ名にエイリアスを設定できる

from random import randint  # randomモジュール内のrandintのみを読み込み

# n = random.random()  # 0以上1未満

# n = random.randint(1, 6)  # ランダムな整数値

# n = r.randint(1, 6) # エイリアスでの呼び出し

n = randint(1, 6)

print(n)
