# 応用的な内容（変数の挙動）

nums = [10, 20, 30]
nums_bak = nums
nums[0] = 100

# 参照がコピーされていることがわかる
print(nums)
print(nums_bak)

# numsの値そのものを代入したい場合はcopyメソッドを使う
nums_bak = nums.copy()


# 2つのリストから辞書をつくる

keys = ["math", "english", "physics"]
values = [62, 91, 84]

scores = {}

# for item in zip(keys, values):  # zip関数でタプルを作る
#     # print(item)
#     key, value = item
#     scores[key] = value

# 上のフローをもっと簡略化
for key, value in zip(keys, values):
    scores[key] = value

# 上のフローをさらに簡略化（リスト内包表記）
scores = {key: value for key, value in zip(keys, values)}

print(scores)
