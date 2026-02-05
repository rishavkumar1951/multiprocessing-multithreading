import time
import multiprocessing


def deposit(balance):
    for i in range(100):
        time.sleep(0.01)
        balance.value = balance.value + 1
        print('++++++++++++++', balance.value)


def withdraw(balance):
    for i in range(100):
        time.sleep(0.01)
        balance.value = balance.value - 1
        print('--------------', balance.value)


if __name__ == "__main__":
    balance = multiprocessing.Value('i', 200)

    d = multiprocessing.Process(target=deposit, args=(balance,))
    w = multiprocessing.Process(target=withdraw, args=(balance,))

    d.start()
    w.start()

    d.join()
    w.join()

    print('Final Value: ', balance.value)

# Every time different final value so, use locking.
