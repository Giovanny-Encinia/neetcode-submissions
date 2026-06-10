class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) <= 1:
            return False

        stack_bracket = []
        valid = {"}": "{", "]": "[", ")": "("}
        closed = set(valid.keys())
        open_ = set(valid.values())

        for letter in s:
            
            if letter in open_:
                stack_bracket.append(letter)

            if letter in closed:
                if stack_bracket and stack_bracket[-1] == valid[letter]:
                    stack_bracket.pop()
                else:
                    return False
        
        if not stack_bracket:
            return True
        
        return False


