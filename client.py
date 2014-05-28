from redis import Redis
from rq import Queue
from worker import count_words_at_url
import time

q = Queue(connection=Redis())
result = q.enqueue(count_words_at_url, "http://graph.facebook.com/vireshas")
time.sleep(2)
print result.result
