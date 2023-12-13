import socket
import time
import random

def main():
    # 目标 IP 地址和端口
    target_ip = '192.168.1.106'
    target_port = 1234

    # 创建 UDP 套接字
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    # 发送数据包的计数器
    packet_count = 0

    try:
        while True:
            # 构建 UDP 数据包
            message = f"UDP Packet {packet_count}".encode('utf-8')

            # 发送数据包
            sock.sendto(message, (target_ip, target_port))

            # 增加计数器
            packet_count += 1

            # 休眠 1 毫秒
            time.sleep(0.001)

    except KeyboardInterrupt:
        # 用户按下 Ctrl+C 时，捕捉 KeyboardInterrupt 异常并退出循环
        pass

    finally:
        # 关闭套接字
        sock.close()

    

# 调用 main() 函数
if __name__ == '__main__':
    main()
