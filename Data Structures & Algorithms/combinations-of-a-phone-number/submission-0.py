class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        """
        6 ! / ((4!)2!) = 6 * 5 / 2 = 3 * 5 = 15

        leters in 3 then letters in 4
        option 
        d
        g h i

        e
        g h i

        f
        g h i

        node -> node -> node
        '342'
        g h i
        j k l
        d e f

        g
        gjd
        gje
        gjf
        """

        search_space = [("a", "b", "c"), ("d", "e", "f"), ("g", "h", "i"),
        ("j", "k", "l"), ("m", "n", "o"), ("p", "q", "r", "s"), ("t", "u", "v"),
        ("w", "x", "y", "z")]

        if not digits:
            return []

        result = []
        def backtrack(i, current_string):
            if len(current_string) == len(digits):
                result.append(current_string)
                return
            
            for letter in search_space[int(digits[i]) - 2]:
                backtrack(i + 1, current_string + letter)


                
        backtrack(0, "")
        return result






