class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        freq = {}
        left = 0 
        window_len = 0
        replacements = 0
        max_freq = 0
        max_len = 0

        for right in range(len(s)):
            char = s[right]
            if char in freq:
                freq[char] += 1
            else:
                freq[char] = 1

            max_freq = max(max_freq, freq[char])
            window_len = (right - left) + 1
            replacements = window_len - max_freq
            
            if replacements > k:
                freq[s[left]] -= 1
                left += 1
            
            window_len = (right - left) + 1
            max_len = max(max_len, window_len)

        return max_len

        

