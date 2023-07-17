# 応用的な内容（複雑なデータ型）

scores = [
    {"name": "Taro", "math": 70, "english": 82},
    {"name": "Jiro", "math": 67, "english": 61},
    {"name": "Saburo", "math": 81, "english": 58},
]

print("Name     Math     English")
print("-------- -------- --------")

# 数学の点数順で並び替え
def compare(score):
    return score["math"]


# scores.sort(key=compare, reverse=True)

# lambda式を使った書き方
scores.sort(key=lambda score: score["math"], reverse=True)

for score in scores:
    # print(score)
    # print(f"{score['name']:8} {score['math']:8} {score['english']:8}")
    for value in score.values():
        print(f"{value:8} ", end="")
    print()
