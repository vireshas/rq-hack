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

#every job has an enqueue id
job_id = "26"
#this is the expected format for a func and its params
job_tuple = "add.add", None, (1,2), {}
#encode with pickle; rq expects pickled value in key "data"
job = {
    "data" : dumps(job_tuple),
}
#push the job; ttl of 500
client.hmset("rq:job:" + job_id, job)
#job is processed as soon as you push the job_id to queue
client.rpush("rq:queue:default", job_id)
#sleep for a while; once processed data is set in redis
time.sleep(2)
#result would be available in key "result"
result = client.hgetall("rq:job:" + job_id)
#decode pickled value before printing
print loads(result["result"])
