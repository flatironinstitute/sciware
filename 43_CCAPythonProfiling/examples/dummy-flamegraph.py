from time import sleep

def a(i):
    sleep(i)

def b():
    for i in range(1,3):
        a(i)
        sleep(1)

def c():
    sleep(1)
    b()

sleep(1)
c()
a(1)