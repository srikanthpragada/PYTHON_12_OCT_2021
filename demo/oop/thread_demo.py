import threading
from threading import Thread

print(threading.current_thread())
print(threading.active_count())


class PrintThread(Thread):
    def run(self):
        for n in range(10):
            print(f'PrintThread {n}')


def print_numbers():
    for n in range(10):
        print(f'Print {n}')


t = PrintThread()
t.start()

t2 = Thread(target=print_numbers)
t2.start()

for n in range(10):
    print(f"Main {n}")
