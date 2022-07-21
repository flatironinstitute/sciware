import signal
import time

def handler(signum, frame):
    print('Why on earth did I make Control-C stop working?!')

signal.signal(signal.SIGINT, handler)

while True:
    print("moo")
    time.sleep(1)
