# ファイルに文字を追記する

file_name = "names2.txt"

names = ["Jiro", "Saburo", "Shiro"]

# 追記したい場合はmodeをa（append）にする
with open(file_name, mode="a") as f:
    for name in names:
        f.write(f"{name}\n")
