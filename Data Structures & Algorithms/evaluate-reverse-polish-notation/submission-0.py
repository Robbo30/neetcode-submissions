class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for c in tokens:
            if c == "+":
                a = stack.pop()
                b = stack.pop()
                result = a + b
                stack.append(result)
            elif c == "-":
                a = stack.pop()
                b = stack.pop()
                result = b - a
                stack.append(result)
            elif c == "*":
                a = stack.pop()
                b = stack.pop()
                result = a * b 
                stack.append(result)
            elif c == "/":
                a = stack.pop()
                b = stack.pop()
                result = int(float(b) / a)
                stack.append(result)
            else:
                stack.append(int(c))
        
        return stack[0]
                