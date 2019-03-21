from collections import deque
import time


class LRU:

    def __init__(self, cache_size=15, expiry_time=10*60):
        self.expiry_time = expiry_time
        self.cache_size = cache_size
        self.cache = {}
        self.cache_queue = deque()

    def reference(self, new_value):

        while len(self.cache_queue) > 0 and self.cache[self.cache_queue[0]] < time.time() - self.expiry_time:
            value = self.cache_queue.pop()
            self.cache.pop(value)

        if not self.cache.__contains__(new_value):
            if len(self.cache_queue) == self.cache_size:
                value = self.cache_queue.popleft()
                self.cache.pop(value)
        else:
            index = 0
            for i, value in enumerate(self.cache_queue):
                if value == new_value:
                    index = i
                    break

            del self.cache_queue[index]

        self.cache_queue.append(new_value)
        self.cache[new_value] = time.time()

    def print_cache(self):
        for elem in self.cache_queue:
            print(elem)

    def test_expiry(self):
        time.sleep(self.expiry_time + 1)
        self.reference("test_val")
        self.print_cache()


cache = LRU(4, 1)
cache.reference(1)
cache.reference(2)
cache.reference(3)
cache.test_expiry()
