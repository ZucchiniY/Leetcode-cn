class Solution:
    def isPalindrome(self, x: int) -> bool:
        x = str(x)
        x1 = x[::-1]
        return x == x1
