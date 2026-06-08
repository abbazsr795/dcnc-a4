def xor(a, b):
    result = []

    for i in range(1, len(b)):
        if a[i] == b[i]:
            result.append('0')
        else:
            result.append('1')

    return ''.join(result)


def mod2div(dividend, divisor):
    pick = len(divisor)

    tmp = dividend[:pick]

    while pick < len(dividend):
        if tmp[0] == '1':
            tmp = xor(divisor, tmp) + dividend[pick]
        else:
            tmp = xor('0' * pick, tmp) + dividend[pick]

        pick += 1

    if tmp[0] == '1':
        tmp = xor(divisor, tmp)
    else:
        tmp = xor('0' * pick, tmp)

    return tmp


def encode_data(data_bits, generator):
    appended_data = data_bits + '0' * (len(generator) - 1)

    remainder = mod2div(appended_data, generator)

    return data_bits + remainder


def verify_data(received_bits, generator):
    remainder = mod2div(received_bits, generator)

    return set(remainder) == {'0'}