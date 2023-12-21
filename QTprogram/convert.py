import random

def hex_to_binary(hex_str):
    try:
        hex_str = hex_str[2:] + hex_str[:2] # 将串口接收的四位数据前后顺序倒换
        decimal_num = int(hex_str, 16)  # 将16进制字符串转换为十进制整数
        binary_str = bin(decimal_num)[2:]  # 将十进制整数转换为二进制字符串，并去掉前缀"0b"
        return binary_str.zfill(16)  # 填充0，确保输出是16位二进制数
    except ValueError:
        return "输入不是有效的16进制数"


def generate_random_binary_sequence(length, probability):
    binary_sequence = [1 if random.random() < probability else 0 for _ in range(length)]
    hex_sequence = []
    for i in range(0, len(binary_sequence), 4):
        four_bits = binary_sequence[i:i+4]
        hex_digit = hex(int(''.join(map(str, four_bits)), 2))[2:]
        hex_sequence.append(hex_digit)


    hex_list = str(hex_sequence)
    return hex_list

if __name__ == "__main__":
    hex_input = "1A3F"  # 你可以替换成你想要转换的16进制数
    binary_output = hex_to_binary(hex_input)
    print("16进制数 {} 的二进制形式是 {}".format(hex_input, binary_output))

    # 生成1024个0或1，生成1的概率为0.5（可以根据需要调整）
    random_sequence = generate_random_binary_sequence(1024, 0.1)

    print("随机生成的16进制序列：", random_sequence)