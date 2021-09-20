"""
思路很简单，如果在序列中，就查直接返回对应的序号；
如果不在序列中，就找到比 target 大的值的位置返回，如果未找到，就返回数组的长度。
"""
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        if target in nums:
            return nums.index(target)
        else:
            for i, num in enumerate(nums):
                if target < num:
                    return i
            else:
                return len(nums)  
