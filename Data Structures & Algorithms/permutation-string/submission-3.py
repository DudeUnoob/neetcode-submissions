class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        if len(s2) < len(s1):
            return False

        
        for i in range(len(s2) - len(s1) + 1):
            
            window = s2[i:i+len(s1)]

            window_counter = Counter(window)

            if window_counter == Counter(s1):
                return True
            
        
        return False