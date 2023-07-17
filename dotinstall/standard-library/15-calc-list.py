# リストを集計する

results = ["pass", "pass", "fail", "pass", "fail", "pass"]

stats = {}
# stats["pass"] += 1
# stats["fail"] += 1

for result in results:
    # 辞書に特定キーが有るか判定。なかったら0で初期化
    if result not in stats:
        stats[result] = 0
    stats[result] += 1

print(stats)
