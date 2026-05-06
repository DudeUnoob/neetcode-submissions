class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        dictS, dictT = {}, {}

        if len(s) != len(t):
            return False

        
        for char in s:
            if char in dictS:
                dictS[char] += 1
            else:
                dictS[char] = 1

        
        for char in t:
            if char in dictT:
                dictT[char] += 1
            
            else:
                dictT[char] = 1

        return dictS == dictT