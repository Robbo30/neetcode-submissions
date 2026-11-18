class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        if not position:
            return 0

        stack = []
        cars = sorted(zip(position, speed), reverse = True)

        for pos, speed in cars:
            time = float(target - pos) / speed
            stack.append(time)
            if len(stack) >= 2 and stack[-1] <= stack[-2]:   # if more than 2 items in the stack (prevents error), and the time is the same or slower then it doesnt make a new fleet so pop it 
                stack.pop()

        return len(stack)
