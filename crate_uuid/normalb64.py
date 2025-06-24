BASE_64_ORDERED_ALPHABET = "+0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ_abcdefghijklmnopqrstuvwxyz/"


def to_base64n(input, pad: bool = True, alphabet=BASE_64_ORDERED_ALPHABET):
    final = ""
    for i in range(0, len(input), 3):
        three_bytes_group = input[i:i + 3]  # Get groups of up to three bytes

        bits = int.from_bytes(three_bytes_group)

        valid_bytes = len(three_bytes_group)  # how many bytes we have.
        padding = (3 - valid_bytes)  # how many bytes are we missing to have 3.

        bits <<= padding * 8  # we push to the left how many bytes we are missing to have 3 bytes (24bits)

        # assert len(bin(bits)) == 24 + 1  # bin returns one extra character 'b'
        for i in range(valid_bytes + 1):  # the valid bytes we have.
            final += alphabet[
                bits >> (18 - (i * 6)) & 0x3F  # Extract 6 bits from the left.
                ]  # https://stackoverflow.com/questions/45220959/python-how-do-i-extract-specific-bits-from-a-byte
        if pad:
            final += '=' * padding
    return final
