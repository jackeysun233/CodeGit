from threading import Thread, current_thread
import threading
import SocketEntity
import uart
import time
import pyqtgraph as pg
countnum = 0
error_data = 0


def target01():
    print("这里是{}".format(current_thread().name))
    global countnum
    countnum = 0
    while True:
        recvdata = None
        recvdata = SocketEntity.myudp()
        print(recvdata)
        if recvdata is not None:
            countnum += 1
            print("======================", recvdata,countnum)
        time.sleep(1)


def target02():
    print("这里是{}".format(current_thread().name))
    while True:
        global error_data
        error_data = uart.myuart("/dev/ttyAMA1", 115200)
        print(error_data)
        time.sleep(1)


def stop():
    flag = False
stop_flag = False



if __name__ == '__main__':
    # 创建线程
    thread01 = Thread(target=target01)
    thread02 = Thread(target=target02)

    # 启动线程
    thread01.start()
    thread02.start()
    # 线程退出
