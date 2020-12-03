# 题目：如果 a + b + c = 1000 且 a^2 +b^2 = c^2 , a b c 都是自然数，如何求出a,b,c的组合
# 使用枚举法

import time # 引入时间，为了计算时间复杂度

start_time = time.time()
# （1）这思路没问题，但是时间复杂度太大
# for a in range(0, 1000):
#     for b in range(0, 1000):
#         for c in range(0, 1000):
#             if a + b + c == 1000 and a**2 + b**2 == c**2:
#                 print("a,b,c:%d,%d,%d" % (a,b,c))

# 思路2：times = 1
for a in range(0, 1000):
    for b in range(0, 1000):
        c = 1000 - a - b
        if a**2 + b**2 == c**2:
                print("a,b,c:%d,%d,%d" % (a,b,c))
end_time = time.time()
print("times:%d" % (end_time - start_time)) # times = 1