"""
这道题思路很清楚，主要是两个点比较重要。
1. 3 的 0 次幂是 1，所以判断如果数小于1就返回False
2. 如果直接取对数，log(n, 3) 遇到 243 时会返回 4.9999999...，导致报错所以要用比值来替代
3. 以某个值为底的对数，然后使用 floor() 返回数据的下舍整数判断是否相等来确认是否为3的倍数
"""


class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        import math
        if n < 1:
            return False
        res = math.log10(n) / math.log10(3)
        return res == math.floor(res)
