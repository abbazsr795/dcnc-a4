def build_packet(data: bytes, crc: int):
    return data + crc.to_bytes(2, byteorder='big')


def split_packet(packet: bytes):
    data = packet[:-2]
    crc = int.from_bytes(packet[-2:], byteorder='big')
    return data, crc