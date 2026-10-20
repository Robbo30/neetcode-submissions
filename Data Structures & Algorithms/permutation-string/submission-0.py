class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_freq, s2_freq = [0] * 26, [0] * 26
        
        if len(s1) > len(s2):
            return False
        
        for i in range(len(s1)):
            s1_freq[ord(s1[i]) - ord("a")] += 1
            s2_freq[ord(s2[i]) - ord("a")] += 1
        
        matches = 0
        for i in range(26):
            if s1_freq[i] == s2_freq[i]:
                matches += 1
        
        left = 0
        for right in range(len(s1), len(s2)):
            if matches == 26:
                return True
            
            right_index = ord(s2[right]) - ord("a")
            s2_freq[right_index] += 1
            if s1_freq[right_index] == s2_freq[right_index]:
                matches += 1
            elif s1_freq[right_index] + 1 == s2_freq[right_index]:
                matches -= 1
            
            left_index = ord(s2[left]) - ord("a")
            s2_freq[left_index] -= 1
            if s1_freq[left_index] == s2_freq[left_index]:
                matches += 1
            elif s1_freq[left_index] - 1 == s2_freq[left_index]:
                matches -= 1
            
            left += 1
        
        return matches == 26
            
            
        

