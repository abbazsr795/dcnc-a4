import socket

from common.crc import verify_crc
from common.packet import split_packet

HOST = "127.0.0.1"
PORT = 5001


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server:
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    server.bind((HOST, PORT))
    server.listen()

    print(f"Server running on {HOST}:{PORT}")

    conn, addr = server.accept()

    with conn:
        print("\nConnected:", addr)

        packet = conn.recv(4096)

        data, received_crc = split_packet(packet)

        print("\nReceived bytes:", data)
        print("Received CRC:", hex(received_crc))

        if verify_crc(data, received_crc):
            print("\nCRC RESULT: VALID")
            print("Decoded message:", data.decode())
            conn.sendall(b"ACK")
        else:
            print("\nCRC RESULT: CORRUPTED")
            conn.sendall(b"NACK")