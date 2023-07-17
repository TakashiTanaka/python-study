# リスト内包表記とifを組み合わせる

prices = [100, 200, 150, 200, 100]

# prices_with_tax = []
# for price in prices:
#     if price != 200:
#         prices_with_tax.append(price * 1.1)

prices_with_tax = [price * 1.1 for price in prices if price != 200]  # 最後にifを加えられる

print(prices_with_tax)
