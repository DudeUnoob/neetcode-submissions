class Solution:
    def countSubstrings(self, s: str) -> int:
        
        total = 0

        for i in range(len(s)):

            for j in range(i + 1, len(s) + 1):

                substring = s[i:j]

                if substring == substring[::-1]:
                    total += 1


        return total