# defaultdictを使う。defaultdict型を使うと、存在しないキーにアクセスした時の挙動を設定できる

from collections import defaultdict

results = ["pass", "pass", "fail", "pass", "fail", "pass"]

# 存在しないキーにアクセスした時の挙動を設定する。0を設定
# def init():
#     return 0

# 事前定義したinit関数を渡す
# stats = defaultdict(init)

# ラムダを渡す
# stats = defaultdict(lambda: 0)

# int関数を渡すと必ず0を返す
stats = defaultdict(int)

for result in results:
    # if result not in stats:
    #     stats[result] = 0
    stats[result] += 1

print(dict(stats))
