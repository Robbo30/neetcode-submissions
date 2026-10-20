class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # max_area = 0 
        # for i in range(len(heights)):
        #     for j in range(i + 1, len(heights)):
        #         w = j - i
        #         area = w * min(heights[i], heights[j])
        #         max_area = max(max_area, area)
        
        # return max_area


        # Real Solution
        max_area = 0
        left = 0 
        right = len(heights) - 1 
        while right > left:
            w = right - left
            h = min(heights[left] , heights[right])
            max_area = max(max_area, w * h)
            if heights[left] < heights[right]:
                left += 1
            elif heights[left] > heights[right]:
                right -= 1
            else:
                left += 1
        
        return max_area
