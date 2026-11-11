class TimeMap:

    def __init__(self):
        self.keyStore = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.keyStore:    # makes a new index for the key, then adds the timestamp and value
            self.keyStore[key] = []
        self.keyStore[key].append([timestamp, value])

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.keyStore:
            return ""
        history = self.keyStore[key]    # gets the history of all timestamps, values for that key/index

        res = ""
        left = 0
        right = len(history) - 1
        while right >= left:    
            mid = (right + left) //2
            if history[mid][0] <= timestamp:    # latest value at or before the timestamp
                res = history[mid][1]
                left = mid + 1
            else:
                right = mid - 1
        
        return res




