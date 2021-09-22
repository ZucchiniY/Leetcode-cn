"""
最终的结果要考虑 Python 的int 类型会比一般语言的长，所以要考虑 32位这个范围。
"""


class Solution:
    def reverse(self, x: int) -> int:
        y = x
        if x < 0:
            y = -1 * x
        y = str(y)[::-1]

        if x < 0:
            r = -1 * int(y)
        else:
            r = int(y)
        return r if -2147483648 < r < 2147483647 else 0
