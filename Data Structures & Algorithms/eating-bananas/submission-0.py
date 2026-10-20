class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left = 1
        right = max(piles)
        res = right

        while left <= right:
            mid = (left + right) // 2 # the speed that koko is eating at per hour
            total_hours = 0

            for pile in piles: # go through each pile and calc hours for that pile and add to total_hours
                total_hours += (pile + mid - 1) // mid 
            
            if total_hours <= h: # if Koko finishes on time (faster or exact time) we save as potential answer and then try see if Koko can go even slower
                res = mid 
                right = mid - 1 
            elif total_hours > h: # if Koko is too slow we need to make it faster so increment left
                left = mid + 1
        
        return res

