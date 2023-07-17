# リストの集計

scores = [10, 20, 30, 20, 40]

print(len(scores))  # 長さ
print(min(scores))  # 最小値
print(max(scores))  # 最大値
print(sum(scores))  # 合計
print(scores.count(20))  # 引数で指定した要素がいくつ入っているかカウント
print(scores.index(20))  # 特定の値がどのインデックスか調べる
print(20 in scores)  # 20がリストの中に存在するか（戻り値は真偽値）
