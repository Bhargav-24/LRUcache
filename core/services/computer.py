from core.utils.cache import LRUcache
import time
class Computer:
    def __init__(self):
        self.lastStatus = None
        self.lastElapsedTime = None
        self.cache = LRUcache(3)
    
    def compute(self, n:int):
        start = time.time()
        ans = self.getAnswer(n)
        end = time.time()
        self.lastElapsedTime = (end - start) * 1000  # Convert to milliseconds
        return ans
    
    def getAnswer(self, n:int):
        if self.cache.contains(n):
            self.lastStatus = "Hit"
            return self.cache.get(n)
        ans = 0
        for i in range(1, n+1):
            ans += i
        self.cache.put(n, ans)
        self.lastStatus = "Miss"
        return ans
    
    def clearCache(self):
        self.cache.clear()