import socket
import random

from common.crc import crc16
from common.packet import build_packet

HOST = "127.0.0.1"
PORT = 5001


def introduce_error(packet: bytearray):
    pos = random.randint(0, len(packet) - 1)

    packet[pos] ^= 0x01  # flip 1 bit

    return packet, pos


message = input("Enter message: ")
data = message.encode()   # REAL BYTES

print("\nOriginal bytes:", data)

crc = crc16(data)

packet = build_packet(data, crc)

packet = bytearray(packet)

corrupt = input("Introduce error? (y/n): ").lower()

if corrupt == 'y':
    packet, pos = introduce_error(packet)
    print(f"\nError introduced at byte index: {pos}")

packet = bytes(packet)

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    s.sendall(packet)

print("\nPacket sent.")