class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        strings = {}
        for s in strs:
            sorted_str = "".join(sorted(s))
            if sorted_str in strings:
                strings[sorted_str].append(s)
            else:
                strings[sorted_str] = [s]
        
        return list(strings.values())
            
