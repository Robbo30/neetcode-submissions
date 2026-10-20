class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # O(n^3) BRUTE FORCE
        # result = []
        # n = len(nums)
        # seen = set()

        # for i in range(n):
        #     for j in range(i + 1, n):
        #         for k in range(j + 1, n):
        #             if nums[i] + nums[j] + nums[k] == 0:
        #                 triple = tuple(sorted([nums[i], nums[j], nums[k]]))
        #                 if triple not in seen:
        #                     seen.add(triple)
        #                     result.append(list(triple))
        # return result


        # O(n) REAL SOLUTION
        nums.sort()
        result = []
        
        for index, i in enumerate(nums):
            left = index + 1
            right = len(nums) - 1
            if index > 0 and i == nums[index - 1]:
                continue

            while left < right:
                curr_sum = i + nums[left] + nums[right]
                if curr_sum > 0:
                    right -= 1
                elif curr_sum < 0:
                    left += 1
                elif curr_sum == 0:
                    result.append([i, nums[left], nums[right]])
                    left += 1
                    while nums[left] == nums[left - 1] and left < right:
                        left += 1
        return result



