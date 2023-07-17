# スライス記法2

nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# 配列要素を切り出す
# sliced_list = nums[2:5]

# 2-8の間で2つとび
# sliced_list = nums[2:8:2]

# 逆向きに2つとび
# sliced_list = nums[8:2:-2]

# 元配列を逆さにしたもの（reverseメソッドの非破壊的表現と言える）
sliced_list = nums[::-1]


print(nums)
print(sliced_list)
