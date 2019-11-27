from queue import Queue
from queue import LifoQueue

if __name__ == "__main__":

    n = 5

    q = Queue()
    s1 = LifoQueue()
    s2 = LifoQueue()

    for i in range(5):
        q.put(i)
        s1.put(i)

    for i in range(5):
        s2.put(s1.get())

    for i in range(5):
        print(q.get(),s2.get())

# q = [0,1,2,3,4] >> 0,1,2,3,4　先頭から
#
# s1 = [0,1,2,3,4] >> 4,3,2,1,0 末尾から
# s2 = [4,3,2,1,0] >> 0,1,2,3,4
