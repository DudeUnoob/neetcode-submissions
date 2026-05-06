class Solution:
    def encode(self, strs: List[str]) -> str:

        if not strs:
            return "!e!"

        else:
            return "!t!".join(strs)

        
    def decode(self, string):
        
        if string == "!e!":
            return []

        txt = string.split("!t!")
        return txt