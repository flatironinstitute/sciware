from time import sleep

def a():
    sleep(5)

def b():
    sleep(1)
    a()

b()