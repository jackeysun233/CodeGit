from threading import Thread, current_thread
import threading


import time
import pyqtgraph as pg
from comm import sendUdp

def target01():
    print('1111')
    # 初始化变量和程序
    count = 0
    ber = 0
    add_ber = 0
    # 设置服务器默认端口号
    RECPORT = 1235
    SENDPORT = 1234

    SENDIP = "10.18.18.105"

    # 发送信息应包含以下
    msg = ""
    num = 256
    for i in range(0, 256):
        msg = msg + "F"
    msg1 = bytes.fromhex(msg)

    # 开启循环发送数据
    while True:
        count += 1
        bit_err_rate = sendUdp(SENDIP, SENDPORT, RECPORT, msg1)
        # 更新误码率
        add_ber = bit_err_rate + add_ber
        ber = add_ber / count
        print('当前误码率为： ', ber)
        count_str = '{:.0f}'.format(count)
        ber_str = '{:.2%}'.format(ber)




def stop():
    flag = False
    stop_flag = False



if __name__ == '__main__':
    # 创建线程
    thread01 = Thread(target=target01)


    # 启动线程
    thread01.start()

    # 线程退出
