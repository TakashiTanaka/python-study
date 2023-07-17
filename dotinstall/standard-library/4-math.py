# 特殊な計算

import math

print(math.sqrt(2))
print(math.ceil(3.5))
print(math.floor(3.5))
print(math.gcd(12, 20, 8))

# roundは注意が必要
print(round(3.5))  # 4
print(round(2.5))  # 2

# 誤差が出る
print(0.1 * 3)

# iscloseで9桁比較して等しいかチェックできる
print(math.isclose(0.1 * 3, 0.3))
