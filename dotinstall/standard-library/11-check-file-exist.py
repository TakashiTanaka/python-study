# ファイルの存在をチェックする

import os

file_name = "names.txt"

# osモジュールのpath.isfileメソッドでファイルの存在をチェック
# if not os.path.isfile(file_name):
#     with open(file_name, mode="w") as f:
#         f.write("Saburo\n")
# else:
#     print("File exist!")

# modeをxにすると、ファイルがすでに存在している場合エラーを投げる
try:
    with open(file_name, mode="x") as f:
        f.write("Saburo\n")
except FileExistsError:
    print("File exist!")
