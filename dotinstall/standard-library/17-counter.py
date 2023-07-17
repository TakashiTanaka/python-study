# Counter
# Counter型を使えば集計がめちゃくちゃ簡単にできる
# ただ集計できるのは単純な構造だけ

from collections import Counter

results = ["pass", "pass", "fail", "pass", "fail", "pass"]

stats = Counter(results)
print(dict(stats))
