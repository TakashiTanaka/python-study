# リストとループの組み合わせ

prices = [100, 200, 150, 200, 100]

# for price in prices:
#     print(price * 1.1)

# インデックス、各要素を収める変数という順番で書かないとだめ
# また、ループさせる配列をenumerateという関数に渡す
for index, price in enumerate(prices):
    print(f"{index}: {price * 1.1:.2f}")
