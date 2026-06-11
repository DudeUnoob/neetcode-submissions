class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.pairs = []

    def get(self, key: int) -> int:
        for i, pair in enumerate(self.pairs):
            if key in pair:
                value = pair[key]

                # move this pair to the end = most recently used
                self.pairs.pop(i)
                self.pairs.append({key: value})

                return value

        return -1

    def put(self, key: int, value: int) -> None:
        for i, pair in enumerate(self.pairs):
            if key in pair:
                # remove old position
                self.pairs.pop(i)

                # re-add at end as most recently used
                self.pairs.append({key: value})
                return

        # key does not exist
        if len(self.pairs) >= self.capacity:
            self.pairs.pop(0)  # remove least recently used

        self.pairs.append({key: value})