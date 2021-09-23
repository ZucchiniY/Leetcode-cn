"""
1. 定义 dp 数组及下标的含义
2. 推导递推公式
3. dp 数组初始化值
4. 遍历顺序

解题思路
判断最长子串的长度，就是先确定外层循环遍历数组的当前值是否大于内层循环的当前值，如果大于则判断前一次内层循环的子序列长度和当前序列长度+1的值，谁更大。
执行完内层循环后，判断内层循环与最大子序列长度的大小。
返回最大子序列大小。
"""
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        nums_len = len(nums)
        if nums_len <= 1:
            return nums_len
        res = 0
        dp = [1] * nums_len
        for i in range(1, nums_len):
            for j in range(0, i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], dp[j] + 1)
            res = max(dp[i], res)
        return res
