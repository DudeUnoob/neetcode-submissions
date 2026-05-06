class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1C, s2C = Counter(s1), Counter(s2)

        if len(s2) < len(s1):
            return False
        

        for i in range(len(s2) - len(s1) + 1):

            window = s2[i:i + len(s1)]
            window_counter = Counter(window)
            s1_counter = Counter(s1)

            if window_counter == s1_counter:
                return True
            else:
                continue

        return False
            