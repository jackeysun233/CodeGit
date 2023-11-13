def hex_to_binary(hex_str):
    try:
        hex_str = hex_str[2:] + hex_str[:2] # 将串口接收的四位数据前后顺序倒换
        decimal_num = int(hex_str, 16)  # 将16进制字符串转换为十进制整数
        binary_str = bin(decimal_num)[2:]  # 将十进制整数转换为二进制字符串，并去掉前缀"0b"
        return binary_str.zfill(16)  # 填充0，确保输出是16位二进制数
    except ValueError:
        return "输入不是有效的16进制数"


if __name__ == "__main__":
    hex_input = "1A3F"  # 你可以替换成你想要转换的16进制数
    binary_output = hex_to_binary(hex_input)
    print("16进制数 {} 的二进制形式是 {}".format(hex_input, binary_output))