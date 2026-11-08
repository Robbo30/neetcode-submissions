class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # speed = 1
        # while True:
        #     time = 0
        #     for pile in piles:
        #         time += (math.ceil(pile / speed))

        #     if time <= h:
        #         return speed
            
        #     speed += 1



        # Real Solution
        left = 1
        right = max(piles) # never needs to eat faster than the biggest pile, bc then every pile takes an hour
        speed = right

        while right >= left:
            mid = (right + left) // 2
            time = 0
            for pile in piles:  # get time for all piles using mid 
                time += (math.ceil(pile / mid))
            
            if time <= h:   # if the time is valid then save it and try slower
                speed = min(speed, mid)
                right = mid - 1
            else:   # if not fast enough then 
                left = mid + 1
        
        return speed
        
        

