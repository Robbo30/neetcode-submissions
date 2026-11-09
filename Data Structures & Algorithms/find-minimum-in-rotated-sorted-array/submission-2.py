class Solution:
    def findMin(self, nums: List[int]) -> int:
        # minimum = 1

        # for num in nums:
        #     minimum = min(minimum, num)

        # return minimum



        # Real Solution
        minimum = nums[0]
        left = 0
        right = len(nums) - 1

        while right >= left:
            if nums[right] > nums[left]:    # the array hasnt rotated so nums[left] is the smallest item 
                minimum = min(minimum, nums[left])
                break
            
            mid = (right + left) // 2
            minimum = min(minimum, nums[mid])

            if nums[mid] >= nums[left]: # if mid is bigger than left, then we are on the left ramp as every value is >= nums[left] and increasing so we want to look at the right ramp only
                left = mid + 1
            else:   # means that we are on the right ramp, so look at left of mid to the right ramp
                right = mid - 1
        
        return minimum


