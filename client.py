from redis import Redis
from rq import Queue
from fb import api
from add import add
import time

q = Queue(connection=Redis())
result = q.enqueue(api, "http://graph.facebook.com/vireshas")
time.sleep(2)
print result.result

result = q.enqueue(add, 1, 2, pubsub="true")
time.sleep(2)
print result.result
