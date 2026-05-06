class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        sett = set()
        left = 0
        longest = 0

        for r in range(len(s)):
            while s[r] in sett:
                sett.remove(s[left])
                left += 1
            
            sett.add(s[r])
            window = (r - left) + 1
            longest = max(window, longest)

        return longest