# ファイルに文字列を書き込む

file_name = "names.txt"

# f = open(file_name, mode="w")
# f.write("Taro\n")
# f.close()

# 上と同じ処理を下記のように書ける
with open(file_name, mode="w") as f:
    f.write("Jiro\n")
