class Solution:
    def isPalindrome(self, s: str) -> bool:
        result_chars = []
        for char in s:
            if char.isalnum():  
                result_chars.append(char.lower())  

        return "".join(result_chars[::-1]) ==  "".join(result_chars)