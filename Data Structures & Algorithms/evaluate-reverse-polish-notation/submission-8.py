class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for letter in tokens:
            result = ""
            if letter.lstrip("-").isnumeric():
                stack.append(int(letter))
            
            elif letter == "+":
                second = stack.pop()
                first = stack.pop()

                result = first + second
                stack.append(result)
            elif letter == "-":
                second = stack.pop()
                first = stack.pop()

                result = first - second
                stack.append(result)
            elif letter == "*":
                second = stack.pop()
                first = stack.pop()

                result = first * second
                stack.append(result)
            elif letter == "/":
                second = stack.pop()
                first = stack.pop()

                result = int(first / second)
                stack.append(result)
            
            print(result)
        
        return stack[-1]
