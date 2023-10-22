import threading
import time


class Worker(threading.Thread):
    def __init__(self, name):
        super().__init__()
        self.name = name

    def run(self):
        print(f"sub thread start {self.name}")
        time.sleep(1)
        print(f"sub thread end {self.name}")


print("main thread start")
for i in range(3):
    name = f"thread {i}"
    t = Worker(name)
    t.start()

print("main thread end")
