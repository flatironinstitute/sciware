import signal
import time

def handler(signum, frame):
    print("There's no stopping this moo train!")

signal.signal(signal.SIGINT, handler)

while True:
    print("moo")
    time.sleep(1)
