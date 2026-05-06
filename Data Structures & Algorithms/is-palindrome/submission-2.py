import re

class Solution:
    def isPalindrome(self, s: str) -> bool:

        s = re.sub(r'\W+', '', s)

        if s[::].lower() == s[::-1].lower():
            return True

        return False