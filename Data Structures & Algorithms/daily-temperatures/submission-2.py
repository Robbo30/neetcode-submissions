class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        result = [0] * len(temperatures)

        for index, temp in enumerate(temperatures):
            while stack and temp > stack[-1][0]:    # if current temp is bigger than prev temp
                stack_temp, stack_index = stack.pop()   # remove prev temp and get index
                result[stack_index] = index - stack_index # calc num of days taken and store at the index       
            stack.append((temp, index)) # add the new temp to the stack
        
        return result
