class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # solutions = set()
        # for i in range(len(nums)):
        #     for j in range(len(nums)):
        #         for k in range(len(nums)):
        #             if i != j and i != k and j != k:
        #                 if nums[i] + nums[j] + nums[k] == 0:
        #                     solutions.add(tuple(sorted([nums[i], nums[j], nums[k]])))
        
        # return [list(t) for t in solutions]


        # Real Solution
        nums.sort()
        solutions = []

        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            left = i + 1 
            right = len(nums) - 1 
            while right > left:
                current = nums[i] + nums[left] + nums[right]
                if current > 0:
                    right -= 1
                elif current < 0:
                    left += 1
                else:
                    solutions.append([nums[i], nums[left], nums[right]])
                    left += 1
                    right -= 1
                
                    while right > left and nums[left] == nums[left - 1]:
                        left += 1
                    while right > left and nums[right] == nums[right + 1]:
                        right -= 1

        return solutions
                

        