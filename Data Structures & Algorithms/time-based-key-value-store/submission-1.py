class TimeMap:

    def __init__(self):

        self.store = defaultdict(list)

        

    def set(self, key: str, value: str, timestamp: int) -> None:
        
        self.store[key].append((value, timestamp))

    def get(self, key: str, timestamp: int) -> str:

        values = self.store[key]

        left = 0
        right = len(values) - 1
        res = ""

        while left <= right:
            middle = (left + right) // 2

            if values[middle][1] <= timestamp:
                res = values[middle][0]
                left = middle + 1

            
            else:
                right = middle - 1

        

        return res
