class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # for i in range(len(nums)):
        #     if nums[i] == target:
        #         return i
        
        # return -1



        # Real Solution
        left = 0
        right = len(nums) - 1

        while right >= left:
            mid = (right + left) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] >= nums[left]:
                if nums[left] <= target and target < nums[mid]:   # if target is between left and mid, then its in the left half so we search left half 
                    right = mid - 1
                else:   # otherwise the target is in the right half
                    left = mid + 1
            else:
                if nums[right] >= target and target > nums[mid]:
                    left = mid + 1
                else:
                    right = mid - 1
        return -1

            
            
