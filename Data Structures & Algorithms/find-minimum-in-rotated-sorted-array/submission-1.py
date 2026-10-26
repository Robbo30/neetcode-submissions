class Solution:
    def findMin(self, nums: List[int]) -> int:
        # minimum = 1

        # for num in nums:
        #     minimum = min(minimum, num)
        # return minimum



        # Real Solution
        result = nums[0]
        left = 0
        right = len(nums) - 1

        while right >= left:
            if nums[right] > nums[left]:
                result = min(result, nums[left])
                break
            
            mid = (right + left) // 2
            result = min(result, nums[mid])

            if nums[mid] >= nums[left]:  # mid is in bigger part so min is after it 
                left = mid + 1
            else:
                right = mid - 1     # mid is in smaller part so min is before it 

        return result