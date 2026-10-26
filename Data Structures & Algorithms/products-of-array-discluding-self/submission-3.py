class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # current = 1
        # products = []

        # for i in range(len(nums)):
        #     current = 1                 # for every product reset to 1
        #     for j in range(len(nums)):
        #         if j != i:              # if indexes are different multiply
        #             current *= nums[j]
        #     products.append(current)

        # return products



        # Real Solution
        products = [1] * len(nums)

        prefix = 1
        for i in range(len(nums)):
            products[i] = prefix
            prefix *= nums[i]
        
        suffix = 1
        for i in range(len(nums) - 1, -1, -1):
            products[i] *= suffix
            suffix *= nums[i]

        return products
