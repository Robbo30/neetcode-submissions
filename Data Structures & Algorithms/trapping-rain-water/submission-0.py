class Solution:
    def trap(self, height: List[int]) -> int:
        # water trapped is the minimum height of the bars to its left and right, minus the bars own height
        left = 0
        left_max = height[left]
        right = len(height) - 1
        right_max = height[right]
        total_water = 0

        while left < right:
            if left_max < right_max:
                left += 1
                left_max = max(left_max, height[left]) 
                total_water += left_max - height[left] #if left wall size is limiting factor we know right side is larger, so we can just use left wall size to calc the water
            elif left_max > right_max:
                right -= 1
                right_max = max(right_max, height[right])
                total_water += right_max - height[right]
            elif left_max == right_max: #can just be else for > and ==
                right -= 1
                right_max = max(right_max, height[right])
                total_water += right_max - height[right]

        return total_water