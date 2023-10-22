from threading import Thread
import time


def work(start, end, result):
    total = 0
    for i in range(start, end):
        total += i
    result.append(total)
    return


START, END = 0, 10000000
result1 = []
result2 = []
startTime = time.time()
# th = Thread(target=work, args=(START, END, result))
th1 = Thread(target=work, args=(START, END // 2, result1))
th2 = Thread(target=work, args=(END // 2, END, result2))

# th.start()
# th.join()
th1.start()
th2.start()
th1.join()
th2.join()
print(time.time() - startTime)


print(f"Result: {result1[0] + result2[0]}")
