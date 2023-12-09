import os, socket
import redis
import time
import random
import logging

logging.basicConfig(level=logging.INFO)

r = redis.StrictRedis(host=os.environ["REDIS_HOST"], port=os.environ["REDIS_PORT"])

hostname = socket.gethostname()


def main():
  while True:
    delay = random.randint(1, 30)
    logging.info("{}: Consumir um item em {} segundos".format(hostname, delay))

    item = r.lpop("queue_matheus")
    logging.info("{}: Consumido o item: {}".format(hostname, item))
    
    time.sleep(delay)

if __name__ == "__main__":
  main()
