class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_word = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        node = self.root

        for letter in word:
            if letter not in node.children:
                node.children[letter] = TrieNode()
            
            node = node.children[letter]
        
        node.is_word = True

    def search(self, word: str) -> bool:
        size_word = len(word)

        def dfs(index, root):
            node = root

            for i in range(index, size_word):
                letter = word[i]

                if letter not in node.children and letter != ".":
                    return False

                if letter != ".":
                    node = node.children[letter]
                else:
                    for child in node.children.values():
                        # the wild card can be each child so we need to check the next letter
                        # if one path is false so try another one
                        if dfs(i + 1, child):
                            return True
                    return False
            
            return node.is_word
        
        return dfs(0, self.root)
        
