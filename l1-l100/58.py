class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s = s.strip(' ')
        e = s.split(' ')[-1]
        return len(e)
