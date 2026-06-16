class Solution:
    def isValid(self, s: str) -> bool:
        
        if len(s) == 0:
            return False

        dict1 = {

            "(": ")",
            "[": "]",
            "{": "}"
        }

        dict2 = {
            ")": "(",
            "]": "[",
            "}": "{"
        }


        stack = []

        for i in s:

            if i in dict2:
                

                if len(stack) == 0:
                    return False

                pop = stack.pop()

                if dict1[pop] == i:
                    continue

                return False

            stack.append(i)
            
        return len(stack) == 0
            