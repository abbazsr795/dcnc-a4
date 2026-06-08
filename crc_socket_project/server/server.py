import socket
import sys
import os

sys.path.append(
    os.path.abspath(
        os.path.join(os.path.dirname(__file__), '..')
    )
)

from common.crc import verify_data

HOST = "127.0.0.1"
PORT = 5000

GENERATOR = "1001"

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server:
    server.bind((HOST, PORT))
    server.listen()

    print(f"Listening on {HOST}:{PORT}")

    conn, addr = server.accept()

    with conn:
        print(f"Connected by {addr}")

        data = conn.recv(4096)

        frame = data.decode()

        print("\nReceived frame:")
        print(frame)

        if verify_data(frame, GENERATOR):
            print("\nCRC Check: DATA NOT CORRUPTED")
        else:
            print("\nCRC Check: DATA CORRUPTED")