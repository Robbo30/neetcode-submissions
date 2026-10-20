class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for c in tokens:
            if c == "+":
                a = stack.pop()
                b = stack.pop()
                stack.append(a + b)
            elif c == "-":
                a = stack.pop()
                b = stack.pop()
                stack.append(b - a)
            elif c == "*":
                a = stack.pop()
                b = stack.pop()
                stack.append(a * b)
            elif c == "/":
                a = stack.pop()
                b = stack.pop()
                stack.append(int(float(b) / a))
            else:
                stack.append(int(c))
        
        return stack[0]
                