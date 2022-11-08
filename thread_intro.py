import threading
import time

def task(i):
    print(f"Task {i} starts")
    time.sleep(1)
    print(f"Task {i} ends")
start = time.perf_counter()
t1 = threading.Thread(target=task, args=[1])
t1.start()
t1.join()

end = time.perf_counter()
print(f"Tasks ended in {round(end - start, 2)} second(s)")

start = time.perf_counter()
t1 = threading.Thread(target=task, args=[1])
t1.start()
t2 = threading.Thread(target=task, args=[2])
t2.start()
t1.join()
t2.join()
end = time.perf_counter()
print(f"Tasks ended in {round(end - start, 2)} second(s)")

T = []
for i in range(100):
    T.append(threading.Thread(target=task, args=[i]))
for i in range(len(T)):
    T[i].start()
for i in range(len(T)):
    T[i].join()