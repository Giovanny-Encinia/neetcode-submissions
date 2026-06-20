class TreeNode:
    def __init__(self):
        self.children = {}
        self.is_word = False

class WordDictionary:

    def __init__(self):
        self.root = TreeNode()

    def addWord(self, word: str) -> None:
        # what happen id word contains dots?

        node = self.root

        for letter in word:
            if letter not in node.children:
                node.children[letter] = TreeNode()
            
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
                
                # what happen if letter id '.' I can move to what children?
                # the word .a. is a valid seach word? what about .. or .
                if letter != ".":
                    node = node.children[letter]
                else:
                    # always the bigger route? what hapen if is dot and then a word?
                    # between two paths the same number of nodes but one is a word and the other is not
                    # apply recursion any?
                    for child in node.children.values():
                        # a..
                        if dfs(i + 1, child):
                            return True
                    return False
            
            return node.is_word
        
        return dfs(0, self.root)
