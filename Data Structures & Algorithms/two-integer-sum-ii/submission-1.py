class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # O(n^2) BRUTE FORCE
        #
        # for i in range(len(numbers)):
        #     for j in range(i + 1, len(numbers)):
        #         if numbers[i] + numbers[j] == target:
        #             return [i + 1, j + 1]
        # return []

        
        # REAL Solution
        left = 0
        right = len(numbers) - 1
        
        while left < right:
            if numbers[left] + numbers[right] > target:
                right -= 1
            elif numbers[left] + numbers[right] < target:
                left += 1
            elif numbers[left] + numbers[right] == target:
                return [left + 1, right + 1]
        return []