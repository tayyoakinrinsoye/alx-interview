def validUTF8(data):
    # Count of remaining bytes in the current character
    remaining_bytes = 0
    
    for byte in data:
        # Check if it's a continuation byte (10xxxxxx)
        if remaining_bytes > 0:
            if (byte >> 6) != 0b10:
                return False
            remaining_bytes -= 1
        else:
            # Check the number of bytes in the current character
            if (byte >> 7) == 0b0:
                remaining_bytes = 0
            elif (byte >> 5) == 0b110:
                remaining_bytes = 1
            elif (byte >> 4) == 0b1110:
                remaining_bytes = 2
            elif (byte >> 3) == 0b11110:
                remaining_bytes = 3
            else:
                return False
    
    # All characters are valid
    return remaining_bytes == 0