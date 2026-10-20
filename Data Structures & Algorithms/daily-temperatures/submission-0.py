class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = len(temperatures) * [0]
        stack = []

        for index, temp in enumerate(temperatures):
            while stack and temp > stack[-1][0]:
                stack_temp, stack_index = stack.pop()
                result[stack_index] = index - stack_index
            stack.append((temp, index))
        
        return result
