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
    time.sleep(delay)

    length = r.llen("queue_matheus")
    if length == 0:
      logging.info("{}: A fila está vazia".format(hostname))
      time.sleep(delay)
      continue

    item = r.lpop("queue_matheus")
    logging.info("{}: Consumido o item: {}".format(hostname, item))
    

if __name__ == "__main__":
  main()
