"""
二分查找，先计算出中间值，如果中间值为 true ，则找中间值替代最大值；
若为 false ，则从 low 下一个开始查找。
"""
class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        low, high = 1, n
        while high > low:
            mid = low + (high - low)//2
            if isBadVersion(mid):
                high = mid
            else:
                low = mid + 1
        return low
