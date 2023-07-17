# ファイルの内容読み込む

file_name = "names3.txt"

# names = ["Taro", "Jiro", "Saburo", "Shiro"]

# with open(file_name, mode="w") as f:
#     for name in names:
#         f.write(f"{name}\n")

with open(file_name, mode="r") as f:
    # names = f.read() # 文字列として取得
    names = f.read().splitlines()  # リストとして取得（各行を要素としたリスト）

print(names)

# 末尾に改行入れたくないときはendオプション
# print(names, end="")
