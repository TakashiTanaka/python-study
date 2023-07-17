# append, extend, insert, clear, remove, pop, del

scores = [10, 20, 30, 40, 20]

print(scores)
scores.append(60)  # メソッド
print(scores)

scores.extend([70, 80])
# scores += [70, 80] # 上と同じ意味

# scores *= 3 # *でリストの内容を繰り返したリストにできる

scores.insert(1, 15)  # 第1引数の位置の前に第2引数で指定した要素を追加する
print(scores)

# scores.clear()  # 全ての要素を削除
# print(scores)

scores.remove(20)  # 引数で指定した要素を削除（添字ではない）また、指定した要素が複数あった場合、最初の要素だけが削除される
print(scores)

popped_item = scores.pop(2)  # 引数で指定したインデックスの要素を削除。またpopメソッドは削除した要素を返す
# popped_item = scores.pop()  # 引数を省略した場合は末尾の要素になる
# del scores[2]  # delでもインデックスを指定して要素を削除できる
print(scores)
print(popped_item)
