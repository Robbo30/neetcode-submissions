class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        
        s1Count, window = {}, {}

        for i in range(len(s1)):
            s1Count[s1[i]] = s1Count.get(s1[i], 0) + 1
            window[s2[i]] = window.get(s2[i], 0) + 1

        if s1Count == window:
            return True
        
        left = 0 
        for right in range(len(s1), len(s2)):
            window[s2[right]] = window.get(s2[right], 0) + 1    # char entering on the right

            window[s2[left]] -= 1   # char leaving on the left 
            if window[s2[left]] == 0:
                del window[s2[left]]
            left += 1

            if s1Count == window:
                return True
            
        return False
        


            