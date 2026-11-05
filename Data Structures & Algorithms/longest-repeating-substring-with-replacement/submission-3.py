class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        max_freq = 0
        freqs = {}
        max_len = 0
        left = 0
        for right in range(len(s)): # get the frequency for every char in the current window of s
            if s[right] in freqs:
                freqs[s[right]] += 1
            else:
                freqs[s[right]] = 1

            max_freq = max(max_freq, freqs[s[right]])   # gets the max current frequency in the window
            window_len = right - left + 1   # gets the current length of the window
            replacements = window_len - max_freq    # gets the amount of replacements needed to make the entire window the same char as the max_freq

            if k >= replacements:   # if we have enough k to make the entire window max_freq char
                max_len = max(max_len, window_len)
            else:
                freqs[s[left]] -= 1
                if freqs[s[left]] == 0:
                    del freqs[s[left]]
                left += 1   # if not we move the window forward
        
        return max_len




