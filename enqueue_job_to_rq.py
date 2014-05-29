"""
    you can push a rq job from a python script
"""
import redis
import json
from functools import partial
import cPickle as pickle
import time

loads = pickle.loads
dumps = partial(pickle.dumps, protocol=pickle.HIGHEST_PROTOCOL)

client = redis.Redis()

job_id = "13"
job_tuple = "w.add", None, (1000,2000), {}
job = {
    "data" : dumps(job_tuple),
}
client.hmset("rq:job:" + job_id, job)
client.rpush("rq:queue:default", job_id)
result = client.hgetall("rq:job:" + job_id)
time.sleep(2)
print result["result"]
