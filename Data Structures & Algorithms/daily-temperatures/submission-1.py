class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        result = [0] * len(temperatures)

        for index, temp in enumerate(temperatures): # get each index, temp pair
            while stack and temp > stack[-1][0]:    # while the stack isnt empty and the most recent temp is bigger than the last temp stored in stack 
                stack_temp, stack_index = stack.pop()   # get the last temp stored and its index
                result[stack_index] = index - stack_index   # add the amount of days taken to find the bigger temp to result stack
            stack.append((temp, index)) # then add the next temp index pair to the stack to be checked
        
        return result