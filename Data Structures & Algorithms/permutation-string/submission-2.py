class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        freq = {}
        for c in s1:
            if c in freq:
                freq[c] += 1
            else:
                freq[c] = 1

        for i in range(0, len(s2) - len(s1) + 1):
            window = s2[i : i + len(s1)]
            window_freq = {}
            for c in window:
                if c in window_freq:
                    window_freq[c] += 1
                else:
                    window_freq[c] = 1
            
            if freq == window_freq:
                return True
        
        return False

        

