def validUTF8(data):
    # Initialize a variable to keep track of the number of bytes in the current character.
    bytes_to_follow = 0

    for byte in data:
        # Check the 8th bit to identify the start of a character.
        if bytes_to_follow == 0:
            if (byte >> 7) == 0b0:
                bytes_to_follow = 0
            elif (byte >> 5) == 0b110:
                bytes_to_follow = 1
            elif (byte >> 4) == 0b1110:
                bytes_to_follow = 2
            elif (byte >> 3) == 0b11110:
                bytes_to_follow = 3
            else:
                return False
        else:
            # Check if the current byte is a continuation byte.
            if (byte >> 6) == 0b10:
                bytes_to_follow -= 1
            else:
                return False

    # If all bytes have been processed correctly, and there are no extra bytes left, it's a valid UTF-8 encoding.
    return bytes_to_follow == 0

