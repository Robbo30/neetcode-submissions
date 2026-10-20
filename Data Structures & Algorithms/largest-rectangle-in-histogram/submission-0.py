class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        max_area = 0

        for i in range(len(heights)): # go through and get every bar as a start point
            start = i 
            while stack and heights[i] < stack[-1][1]: # go right until stack is empty OR we see a bigger bar
                start_index, height = stack.pop() # remove tallest bar as the small bar we are now on acts as a limiter to the max_area
                area = (i - start_index) * height # calc area and see if its max
                max_area = max(max_area, area)
                start = start_index # update the start of the rectangle
            
            stack.append((start, heights[i])) # add the new bar to the stack
        
        while stack: # some bars will be left in stack as they werent cut off by a shorter bar
            start_index, height = stack.pop() 
            area = (len(heights) - start_index) * height 
            max_area = max(max_area, area)
        
        return max_area

        


