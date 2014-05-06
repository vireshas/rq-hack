from redis import Redis
from rq import Queue

q = Queue(connection=Redis())

from worker import count_words_at_url

result = q.enqueue(count_words_at_url, "http://graph.facebook.com/vireshas")
import pdb; pdb.set_trace()
print result.perform()
