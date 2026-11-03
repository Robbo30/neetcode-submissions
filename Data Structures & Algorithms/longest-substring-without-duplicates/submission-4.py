class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # max_len = 0

        # for i in range(len(s)):
        #     chars = set()
        #     for j in range(i , len(s)):
        #         if s[j] in chars:
        #             break
        #         chars.add(s[j])
        #     max_len = max(max_len, len(chars))
        
        # return max_len



        # Real Solution
        max_len = 0
        left = 0 
        right = 0
        chars = set()

        while right < len(s):   # while right is valid 
            if s[right] not in chars:   # if the char isnt in chars, add it and see if the window length is bigger than the previous largest and move right forwards to continue looking
                chars.add(s[right])
                max_len = max(max_len, right - left + 1)
                right += 1
            else:
                chars.remove(s[left])   # if char is already in chars, then we remove the last element in chars as thats guranteed to be where the duplicate of it is stored
                left += 1   # move forward the left pointer as we removed a char
        
        return max_len
