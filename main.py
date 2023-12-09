import os
import redis

r = redis.StrictRedis(host=os.environ["REDIS_HOST"], port=os.environ["REDIS_PORT"])

# FIFO
r.rpush("q_matheus", "Hello World!!")