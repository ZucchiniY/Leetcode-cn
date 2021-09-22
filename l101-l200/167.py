"""
二分法解法：时间慢，输入列表中查找中间值，

如果大于目标值，则左移——右指针减一；如果小于目标值则右移——左指针加一。
"""


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        n = len(numbers)
        for i in range(n - 1):
            l, r = i + 1, n - 1
            while l <= r:
                mid = (l + r) // 2
                if numbers[mid] == target - numbers[i]:
                    return [i + 1, mid + 1]
                elif numbers[mid] > target - numbers[i]:
                    r = mid - 1
                else:
                    l = mid + 1


"""
双指针解法：时间中，输入列表中分别进行左右移。
在左指针小于等于右指针时，如果值小于目标值，左指针右移；如果大于目标值，右指针左移。
"""


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        n = len(numbers)
        l, r = 0, n - 1
        while l <= r:
            if numbers[l] + numbers[r] == target:
                return [l + 1, r + 1]
            elif numbers[l] + numbers[r] < target:
                l += 1
            else:
                r -= 1


"""
哈希表解法：速度快，将对应差值存入哈希表中。
判断当前值是否在哈希表中存在，若在，则说明存在配对数据，返回哈希表中的值（存入数据列表的索引值）和当前索引。
不存在则计算目标值差存到字典中。
"""


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        hash_ = dict()
        for index, num in enumerate(numbers):
            if num in hash_:
                return [hash_[num] + 1, index + 1]
            hash_[target - num] = index
