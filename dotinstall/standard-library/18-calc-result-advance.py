# 更に複雑な集計

from collections import defaultdict

results = [
    ("pass", "Taro"),
    ("pass", "Jiro"),
    ("fail", "Saburo"),
    ("pass", "Shiro"),
]

stats = defaultdict(list)

for result, name in results:
    stats[result].append(name)

print(dict(stats))
