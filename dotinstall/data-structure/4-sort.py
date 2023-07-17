# 並び替え

scores = [10, 20, 30, 40, 20]

# scores.reverse() # 逆順に並び替え
# print(scores)

# scores.sort()  # 小さい順に並び替え
# print(scores)

# scores.sort(reverse=True)  # 大きい順に並び替え
# print(scores)

scores_sorted = sorted(scores, reverse=True)  #  元のリストを変更せずに、ソートしたリストを返す
print(scores)
print(scores_sorted)
