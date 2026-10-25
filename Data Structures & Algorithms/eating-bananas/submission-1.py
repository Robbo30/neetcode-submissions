class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # speed = 1
        # while True:
        #     time = 0
        #     for pile in piles:
        #         time += math.ceil(pile / speed)
            
        #     if time <= h:
        #         return speed
        #     speed += 1

        # return speed


        # Real Solution
        l = 1
        r = max(piles)
        speed = r

        while r >= l:
            m = (r + l) // 2
            time = 0
            for pile in piles:
                time += math.ceil(pile / m)
            
            if time > h:
                l = m + 1
            else:
                speed = min(speed, m)
                r = m - 1   
        
        return speed