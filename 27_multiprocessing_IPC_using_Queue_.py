from multiprocessing import Process, Queue
import time

# Function for the producer process
def producer(q):
    print("Producer: generating data...")
    for i in range(5):
        q.put(f"Message {i}")   # put data into the queue
        print(f"Producer: sent Message {i}")
        time.sleep(1)           # simulate work
    q.put(None)  # signal end of data

# Function for the consumer process
def consumer(q):
    while True:
        msg = q.get()   # receive data from the queue
        if msg is None: # end signal
            print("Consumer: no more messages, exiting.")
            break
        print(f"Consumer: received {msg}")

if __name__ == "__main__":
    q = Queue()

    # Create two separate processes
    p1 = Process(target=producer, args=(q,))
    p2 = Process(target=consumer, args=(q,))

    # Start both processes
    p1.start()
    p2.start()

    # Wait for them to finish
    p1.join()
    p2.join()

    print("Main process: done.")