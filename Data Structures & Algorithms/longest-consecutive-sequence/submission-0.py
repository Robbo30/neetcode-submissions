class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        longest = 0

        for num in num_set:
            if (num - 1) not in num_set:
                curr_streak = 1
                next_num = num + 1
                while next_num in num_set:
                    curr_streak += 1
                    next_num += 1
                longest = max(longest, curr_streak)
        
        return longest