class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # for i in range(len(numbers)):
        #     for j in range(len(numbers)):
        #         if i != j:
        #             if numbers[i] + numbers[j] == target:
        #                 return [i + 1, j + 1]


        # Real Solution
        left = 0
        right = len(numbers) - 1
        while right > left:
            num = numbers[left] + numbers[right]
            if num > target:
                right -= 1
            elif num < target:
                left += 1
            else:
                return [left + 1, right + 1]
