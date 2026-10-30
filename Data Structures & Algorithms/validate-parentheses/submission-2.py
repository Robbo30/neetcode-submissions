class Solution:
    def isValid(self, s: str) -> bool:
        closeToOpen = {")": "(", "]" : "[", "}" : "{"}
        stack = []

        for c in s:
            if c in closeToOpen:
                if stack and stack[-1] == closeToOpen[c]:   # if stack isnt empty and the most recent item added is the opener for the current closer then correct so we remove
                    stack.pop()
                else:
                    return False    # if not correct return False
            else:
                stack.append(c) # not in stack so add

        if not stack:   # if is empty then all brackets are closed so return true
            return True
        else:
            return False