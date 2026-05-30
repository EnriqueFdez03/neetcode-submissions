class TimeMap:



    def __init__(self):
        self.hashmap = dict()

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key in self.hashmap:
            self.hashmap[key].append((value, timestamp))
        else:
            self.hashmap[key] = [(value, timestamp)]

    def get(self, key: str, timestamp: int) -> str:
        if not key in self.hashmap:
            return "" 
        
        # binary search
        values = self.hashmap[key]
        l, r = 0, len(values) - 1

        candidate = ""
        mostRecent = 0
        while l <= r:
            m = l + ((r - l) // 2)

            if values[m][1] <= timestamp:
                if values[m][1] > mostRecent:
                    mostRecent = values[m][1]
                    candidate = values[m][0]
                l = m + 1
            else:
                r = m - 1
        
        return candidate
