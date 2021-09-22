"""
原地翻转解法：原地翻转，重点在原地二字。
如果直接将值进行替换的话，会因为值的覆盖导致结果是由第一次翻转的数据处理的结果。
所以如何在不改变值的时候进行翻转才是最大的问题。

运算时，先将整个序列倒序排列，然后在 k 的位置上进行前后的倒序，返回目标值。
"""


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k = k % len(nums)
        nums[:] = nums[::-1]
        nums[:k] = nums[:k][::-1]
        nums[k:] = nums[k:][::-1]
