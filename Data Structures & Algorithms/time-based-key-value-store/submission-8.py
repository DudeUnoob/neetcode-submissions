class TimeMap:

    def __init__(self):
        
        self.store = { None: None }
        

    def set(self, key: str, value: str, timestamp: int) -> None:

        if key not in self.store:
            self.store[key] = [(value, timestamp)]

        self.store[key].append((value, timestamp))

    def get(self, key: str, timestamp: int) -> str:
        
        #return most recent value of key if set prev called and most recent timestamp
        # for key that prev_timestamp is <= timestamp

        # binary search on values

        if key not in self.store:
            return ""
        
        values = self.store[key]

        left = 0
        right = len(values) - 1

        # for i in values:
        #     print(i) -> ex: ('happy', 1)
        res = ""
        while left <= right:
            mid = (left + right) // 2

            if values[mid][1] <= timestamp:
                res = values[mid][0]

                left = mid + 1
            
            else:
                right = mid - 1

        return res



