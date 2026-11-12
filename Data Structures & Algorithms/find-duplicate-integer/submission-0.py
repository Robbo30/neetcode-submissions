class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # seen = set()
        # for num in nums:
        #     if num in seen:
        #         return num
        #     else:
        #         seen.add(num)



        # Real Solution
        slow = 0 
        fast = 0

        while True: # the point where slow == fast is the meeting point in the cycle
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break
        
        slow2 = 0
        while True: # then use old pointer and meeting point pointer, and where they meet again is the cycles entrance which is also the duplicate number
            slow2 = nums[slow2]
            slow = nums[slow]
            if slow2 == slow:
                return slow

        
