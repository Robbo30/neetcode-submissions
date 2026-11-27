class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        longest = 0

        for num in num_set:
            if (num - 1) not in num_set: # if True then the num is a starter (has no consecutive number before it)
                length = 1 
                while (num + 1) in num_set: # keep adding one until next consecutive number isnt in the num_set, meaning sequence has ended
                    length += 1
                    num += 1
                longest = max(longest, length)
        
        return longest
