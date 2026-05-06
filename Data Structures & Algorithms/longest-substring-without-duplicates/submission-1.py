class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        left = 0
        ha = set()
        length = 0

        for r in range(len(s)):
            while s[r] in ha:
                ha.remove(s[left])
                left += 1
            
            ha.add(s[r])
            length = max(length, r - left + 1)

        return length
            
