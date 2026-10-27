class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        new_s = ""

        for ch in s:
            if ch.isalnum():
                new_s += ch.lower()


        s = new_s

        left = 0
        right = len(s) - 1

        while left < right:

            if s[left] == s[right]:
                left += 1
                right -= 1

            else:
                return False

        return True
            
