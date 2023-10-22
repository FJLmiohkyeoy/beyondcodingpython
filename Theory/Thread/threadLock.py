import threading
import time

shared_number = 0

lock = threading.Lock()


def work(number):
    global shared_number
    print(f"number = {number}")

    lock.acquire()
    for i in range(number):
        shared_number += 1
    lock.release()


threads = []
start_time = time.time()
for i in range(2):
    t = threading.Thread(target=work, args=(50000000,))
    t.start()
    threads.append(t)

for t in threads:
    t.join()

print(f"{time.time() - start_time} seconds")
print(f"shared_number={shared_number}")
print("end of main")
