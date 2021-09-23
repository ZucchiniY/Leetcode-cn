"""
复制的次数等分解质因数的次数，分解质因数的计算，主要有两个，递归和质数求解。

这里要使用 while 进行循环，而不能使用 for 因为 n 的次数会变。
"""


class Solution:
    def minSteps(self, n: int) -> int:
        res = 0
        if n == 1:
            return res
        d = 2
        while n > 1:
            while (n % d == 0):
                res += d
                n //= d
            d += 1
        return res


"""
递归方式求解

如果能整除就调用方法本身，直到返回 0 的时候。
"""


class Solution:
    def minSteps(self, n: int) -> int:
        res = 0
        if n == 1:
            return res
        for i in range(2, n):
            if n % i == 0:
                return self.minSteps(n // i) + i
        return n
