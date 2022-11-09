import time
import multiprocessing

def task(i):
    print(f"Task {i} starts for 1 second")
    time.sleep(1)
    print(f"Task {i} ends")
if __name__ == '__main__':
    start = time.perf_counter()
    p1 = multiprocessing.Process(target=task, args=)
    p2 = multiprocessing.Process(target=task)
    p1.start()
    p2.start()
    p1.join()
    p2.join()
    end = time.perf_counter()
    print(f"Tasks ended in {round(end - start, 2)} second(s)")