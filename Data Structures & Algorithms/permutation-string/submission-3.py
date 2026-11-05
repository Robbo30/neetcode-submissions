class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # freq = {}
        # for c in s1:
        #     if c in freq:
        #         freq[c] += 1
        #     else:
        #         freq[c] = 1
        
        # for i in range(0, len(s2) - len(s1) + 1):  
        #     window = s2[i : i + len(s1)]
        #     window_freqs = {}
        #     for c in window:
        #         if c in window_freqs:
        #             window_freqs[c] += 1
        #         else:
        #             window_freqs[c] = 1
            
        #     if freq == window_freqs:
        #         return True
        
        # return False



        # Real Solution
        if len(s1) > len(s2):   # if the length of the substring is bigger than the string we're looking at then its impossible there is a permutation
            return False

        s1Count = {}
        window = {}

        for i in range(len(s1)):    # gets freq of s1 and compares to the first sub str of s2
            s1Count[s1[i]] = s1Count.get(s1[i], 0) + 1
            window[s2[i]] = window.get(s2[i], 0) + 1
        
        if s1Count == window:
            return True
        
        left = 0
        for right in range(len(s1), len(s2)):   # checks all other sub strings
            window[s2[right]] = window.get(s2[right], 0) + 1  # adds the new char coming in on the right
            window[s2[left]] -= 1   # removes the char leaving on the left
            if window[s2[left]] == 0:
                del window[s2[left]]
            left += 1
            
            if s1Count == window:
                return True
        
        return False
            
            
 

        

