class Solution:
    def isPalindrome(self, s: str) -> bool:
        # new_str = ""
        # for char in s:
        #     if char.isalnum():
        #         new_str += char.lower()
        
        # return new_str == new_str[::-1]


        left = 0 
        right = len(s) - 1

        while right > left:
            while right > left and not s[left].isalnum():
                left += 1
            while right > left and not s[right].isalnum():
                right -= 1
            if s[left].lower() != s[right].lower():
                return False
            
            left += 1
            right -= 1
        
        return True


