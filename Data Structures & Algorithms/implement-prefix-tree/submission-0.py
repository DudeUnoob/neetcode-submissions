class TrieNode:

    def __init__(self):
        self.children = {}
        self.endOfWord = False


class PrefixTree:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        node = self.root
        
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()


            node = node.children[char]

        node.endOfWord = True




    def search(self, word: str) -> bool:
        
        node = self.root

        for char in word:
            if char not in node.children:
                return False
            
            else:
                node = node.children[char]

        return node.endOfWord

    def startsWith(self, prefix: str) -> bool:
        
        curr = self.root

        for char in prefix:
            if char not in curr.children:
                return False

            curr = curr.children[char]

        return True
        