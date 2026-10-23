class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        freqs = {}
        max_freq = 0
        current_len = 0
        longest = 0
        left = 0

        for right in range(len(s)):
            if s[right] in freqs:   # get frequency of all chars in the window
                freqs[s[right]] += 1
            else:
                freqs[s[right]] = 1

            max_freq = max(max_freq , freqs[s[right]])  # gets the highest freq of a char in the current window

            if (right - left + 1) - max_freq > k:   # if the length of the window - the most freq char is more than k, then the window is invalid as not enough changes to make the whole window the same char
                freqs[s[left]] -= 1
                left += 1   # decrease the freq of char leaving the window, and increment left
            
            current_len = right - left + 1
            longest = max(longest, current_len) # calculates the current window length and compares to current longest window 

        return longest

            