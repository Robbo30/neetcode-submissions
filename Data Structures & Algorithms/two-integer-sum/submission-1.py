class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # for i in range(len(nums)):
        #     for j in range(len(nums)):
        #         if i != j:
        #             if nums[i] + nums[j] == target:
        #                 return [i, j]



        numbers = {}
        for i in range(len(nums)):
            needed = target - nums[i]
            if needed in numbers:
                return [numbers[needed], i]
            numbers[nums[i]] = i

        
