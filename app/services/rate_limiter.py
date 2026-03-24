import time

class RateLimiter:
    ##limit → max requests
    ##window → time window in seconds
    def __init__(self, limit=5, window=60):
        self.requests = [] ## Store userId with timestamps so that the window can be maintained
        self.limit = limit
        self.window = window

    def allow(self, user_id: str):
        now = time.time()

        if user_id not in self.requests:
            self.requests[user_id] = []

        # Sliding window. At at time, store only the last 60 seconds items
        self.requests[user_id] = (
            t for t in self.requests[user_id]
            if now - t < self.window 
        )

        if len(self.requests[user_id]) > self.limit:
            return False
        
        self.requests[user_id].append(now)
        return True
    