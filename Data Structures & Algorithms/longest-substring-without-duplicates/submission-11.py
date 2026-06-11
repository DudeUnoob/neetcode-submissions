class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        res = 0

        l = 0

        seen = set()

        #Let's say zxy are in set
        for r in range(len(s)):

            while s[r] in seen:
                seen.remove(s[l])
                l += 1
            
            seen.add(s[r])
            res = max(res, r - l + 1)

        return res




        
