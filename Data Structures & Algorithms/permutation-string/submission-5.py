class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        dictS2 = defaultdict(int)

        for k in s1:

            dictS2[k] += 1
        
        for i in range(len(s2) - len(s1) + 1):

            view = s2[i: i + len(s1)]

            dictS1 = defaultdict(int)

            for j in view:

                dictS1[j] +=1


            if(dictS1 == dictS2):
                return True

        return False

            
