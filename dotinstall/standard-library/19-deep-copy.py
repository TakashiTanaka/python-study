# 深いコピー

import copy

# nums = [10, 20, 30]
# nums_bak = nums.copy()
# nums[0] = 100
# print(nums)
# print(nums_bak)

# リストの中にmutableなデータ型があった場合、浅いコピーになってしまう
nums = [10, 20, 30, [40, 50]]
# nums_bak = nums.copy() # 浅いコピー
nums_bak = copy.deepcopy(nums)  # 深いコピー
nums[3][0] = 100
print(nums)
print(nums_bak)
