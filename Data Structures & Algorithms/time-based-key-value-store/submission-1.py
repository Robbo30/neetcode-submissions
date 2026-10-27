class TimeMap:

    def __init__(self):
        self.keyStore = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.keyStore:
            self.keyStore[key] = []
        self.keyStore[key].append([timestamp, value])

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.keyStore:    # if the key isnt in the dict then return nothing
            return ""
        history = self.keyStore[key]    # gets all of the pairs at that key

        left = 0 
        right = len(history) - 1
        res = ""

        while right >= left:
            mid = (right + left) // 2
            if history[mid][0] <= timestamp:    # if the current timestamp is less than or equal to the wanted timestamp then we update the result
                res = history[mid][1]
                left = mid + 1
            else:
                right = mid - 1
        
        return res


