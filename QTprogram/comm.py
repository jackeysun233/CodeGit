import socket
import time
import serial
import re


def hex_to_binary(byte_str):
    hex_str = byte_str.hex()
    hex_str = hex_str[2:] + hex_str[:2] # 将串口接收的四位数据前后顺序倒换
    decimal_num = int(hex_str, 16)  # 将16进制字符串转换为十进制整数
    # binary_str = bin(decimal_num)[2:]  # 将十进制整数转换为二进制字符串，并去掉前缀"0b"
    return decimal_num  # 填充0，确保输出是16位二进制数



def sendUdp(SENDIP, SENDPORT, RCVPORT,msg):

    BITNUM = 1024 # 定义每个字节中的比特数量


    # 初始化网口和串口的监听
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # 创建UDP的socket套接字
    client_socket.bind(('', RCVPORT)) # 绑定UDP的接收端口
    server_address = (SENDIP, SENDPORT) # FPGA的IP地址

    ser = serial.Serial('/dev/ttyAMA1', 115200, timeout=0.1) # 创建UART监听接口

    client_socket.sendto(msg, server_address) # 向FPGA发送UDP数据包
    data = ser.readline() # 读FPGA串口数据
    receive_data, client = client_socket.recvfrom(1024) # 读FPGA网口数据

    client_socket.close() # 关闭网口的套接字

    if data:

        err_curr_byte = hex_to_binary(data) # 将串口接受的字节码转换为10进制整型，得到误码率

        print("当前字节的误码数量为: ",err_curr_byte)

    bit_err_rate = err_curr_byte / BITNUM

    return bit_err_rate

    # print("来自客户端%s,发送的%s" % (client, receive_data.hex()))





if __name__ == "__main__":
    # 设置服务器默认端口号
    RECPORT = 1235
    SENDPORT = 1234
    RECIP = "10.18.18.106"
    SENDIP = "10.18.18.105"
    # 发送信息应包含以下
    msg = ""
    num = 256
    for i in range(0, 256):
        msg = msg + "F"
    msg1 = bytes.fromhex(msg)

    while True:

        sendUdp(SENDIP, SENDPORT,RECPORT, msg1)
