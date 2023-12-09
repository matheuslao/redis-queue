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
    logging.info("Gerar um item em {} segundos".format(delay))
    time.sleep(delay)

    item_number = len(r.lrange("queue_matheus", 0, -1)) + 1
    r.rpush("queue_matheus", "item {}".format(item_number))
    logging.info("{}: Gerado o item: {}".format(hostname, item_number))

  

if __name__ == "__main__":
  main()
