from collections import defaultdict

class RateLimiter:
    def __init__(self, max_requests: int, window_seconds: int):
        self.max_requests=max_requests
        self.window_seconds=window_seconds
        self.request_manager=defaultdict(defaultdict)

    def allow(self, user_id: str, t: int) -> bool:
        self.evict_old(t,user_id)
        currentcount= len(self.request_manager[user_id].keys())

        if currentcount < self.max_requests:
          self.request_manager[user_id][t]=currentcount+1
          return True
        else:
            return False
        

    def evict_old(self,timestamp,user_id):
        if user_id in self.request_manager.keys():
            oldtime=timestamp-self.window_seconds
            keylist=[]
            if oldtime >0:
                for key in self.request_manager[user_id]:
                    if key< oldtime:
                        keylist.append(key)

            for key in keylist:
                del self.request_manager[user_id][key]
    



r=RateLimiter(3,10)
print(r.allow("u1", t=1))# → True (1st request)
print(r.allow("u1", t=2))# → True (2nd request)
print(r.allow("u1", t=3)) # → True (3rd request)
print(r.allow("u1", t=5)) # → False (4th request within 10s of the first — exceeds limit)
print(r.allow("u1", t=12))