class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for c in tokens:
            if c in "+-*/":
                a = stack.pop()
                b = stack.pop()
                if c == "+":
                    stack.append(a + b)
                elif c == "-":
                    stack.append(b - a)
                elif c == "*":
                    stack.append(a * b)
                elif c == "/":
                    stack.append(int(float(b) / a))
            else:
                stack.append(int(c))
        
        return stack[0]