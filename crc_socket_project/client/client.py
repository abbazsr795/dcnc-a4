import socket
import sys
import os

sys.path.append(
    os.path.abspath(
        os.path.join(os.path.dirname(__file__), '..')
    )
)

from common.crc import encode_data
from common.packet import string_to_binary

HOST = "127.0.0.1"
PORT = 5000

GENERATOR = "1001"

message = input("Enter message: ")

binary_message = string_to_binary(message)

encoded_message = encode_data(binary_message, GENERATOR)

print("\nEncoded frame:")
print(encoded_message)

corrupt = input(
    "\nCorrupt transmission? (y/n): "
).lower()

if corrupt == 'y':
    bit_list = list(encoded_message)

    bit_list[5] = (
        '1' if bit_list[5] == '0'
        else '0'
    )

    encoded_message = ''.join(bit_list)

    print("\nCorrupted frame:")
    print(encoded_message)

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client:
    client.connect((HOST, PORT))

    client.sendall(encoded_message.encode())

print("\nFrame sent.")