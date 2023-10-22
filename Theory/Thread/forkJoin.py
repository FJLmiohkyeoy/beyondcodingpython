import threading
import time


class Worker(threading.Thread):
    def __init__(self, name):
        super().__init__()
        self.name = name

    def run(self):
        print(f"sub thread start {self.name}")
        time.sleep(1)
        print(f"sub thread end {threading.currentThread().getName()}")


print("main thread start")

threads = []
for i in range(3):
    thread = Worker(i)
    thread.start()
    threads.append(thread)

for thread in threads:
    thread.join()

print("main thread post job")
print("main thread end")
