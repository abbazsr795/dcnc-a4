def crc16(data: bytes, poly=0x1021):
    crc = 0xFFFF

    for byte in data:
        crc ^= (byte << 8)

        for _ in range(8):
            if crc & 0x8000:
                crc = (crc << 1) ^ poly
            else:
                crc <<= 1

            crc &= 0xFFFF

    return crc


def verify_crc(data: bytes, received_crc: int):
    return crc16(data) == received_crc