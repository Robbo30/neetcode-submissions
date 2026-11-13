class Solution:
    def isValid(self, s: str) -> bool:
        closeToOpen = {")": "(", "]" : "[", "}" : "{"}
        stack = []

        for c in s:
            if c in closeToOpen:
                if stack and stack[-1] == closeToOpen[c]:   # if the stack isnt empty AND it the most recent item is the opposite of the current bracket then its valid so we remove it
                    stack.pop()
                else:
                    return False    # the most recent bracket wasnt closed so false
            else:
                stack.append(c) # not in the stack so we add the bracket

        if not stack:
            return True
        else:
            return False