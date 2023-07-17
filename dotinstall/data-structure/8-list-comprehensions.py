# リスト内包表記

prices = [100, 200, 150, 200, 100]

# prices_with_tax = []
# for price in prices:
#     prices_with_tax.append(price * 1.1)

prices_with_tax = [price * 1.1 for price in prices]  # ループ処理の前にリストに追加したい要素を書く

print(prices_with_tax)
