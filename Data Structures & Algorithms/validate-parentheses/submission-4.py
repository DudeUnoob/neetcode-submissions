class Solution:
    def isValid(self, s: str) -> bool:

        stack = []


        left_parentheses, right_parentheses = "(", ")"
        left_squareBracket, right_squareBracket = "[", "]"
        left_curlyBracket, right_curlyBracket = "{", "}"

        parentheses_dic_2 = {
            left_parentheses: right_parentheses,
            left_squareBracket: right_squareBracket,
            left_curlyBracket: right_curlyBracket
        }

        if len(s) == 0 or s[0] == ")" or s[0] == "]" or s[0] == "}":
            return False


        for i in s:
            if i == right_curlyBracket or i == right_parentheses or i == right_squareBracket:

                if len(stack) == 0:
                    return False

                pop = stack.pop()

                if parentheses_dic_2[pop] == i:
                    continue

                return False

            stack.append(i)
        return len(stack) == 0




        