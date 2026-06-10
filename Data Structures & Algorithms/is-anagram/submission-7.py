class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        dictS, dictT = defaultdict(int), defaultdict(int)

        print(dict)

        for i in s:
            dictS[i] += 1

        for j in t:
            dictT[j] += 1

        return dictS == dictT