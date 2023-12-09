import os
import redis
import time
import random
import logging

logging.basicConfig(level=logging.INFO)

r = redis.StrictRedis(host=os.environ["REDIS_HOST"], port=os.environ["REDIS_PORT"])

def main():
  while True:
    delay = random.randint(1, 30)
    logging.info("Gerar um item em {} segundos".format(delay))

    item_number = len(r.lrange("queue_matheus", 0, -1)) + 1
    r.rpush("queue_matheus", "item {}".format(item_number))

    time.sleep(delay)

if __name__ == "__main__":
  main()
