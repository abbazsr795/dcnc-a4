def string_to_binary(text):
    return ''.join(format(ord(c), '08b') for c in text)


def binary_to_string(binary):
    chars = []

    for i in range(0, len(binary), 8):
        byte = binary[i:i+8]
        chars.append(chr(int(byte, 2)))

    return ''.join(chars)