class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        sq_nums = []
        for num in nums:
            new = num * num
            sq_nums.append(new)
        sq_nums.sort()
        return sq_nums
