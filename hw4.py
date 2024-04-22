from PIL import Image

def extract_lsb(image_path):
    img = Image.open(image_path)
    width, height = img.size

    binary_message = ""
    message_end_count = 0  # Count the number of consecutive newline characters encountered
    utf8_message = ""

    for y in range(height):
        for x in range(width):
            pixel = img.getpixel((x, y))
            # Extract the LSB of each color channel (RGB) while ignoring the alpha channel
            lsb = tuple(bit & 1 for bit in pixel[:3])
            # Convert LSB tuple to binary string
            lsb_string = ''.join(str(bit) for bit in lsb)
            # Append LSB string to the message
            binary_message += lsb_string

            # Check if the end of the message is reached
            if binary_message.endswith('0000101000001010'):  # Check for two consecutive newline characters
                message_end_count += 1
                if message_end_count == 2:
                    return binary_message[:-16]  # Remove the two trailing newline characters
            else:
                message_end_count = 0  # Reset the count if newline characters are not encountered
            
            # # Check if a full byte has been captured
            # if len(binary_message) >= 8:
            #     # Convert the first 8 bits to an integer
            #     byte_value = int(binary_message[:8], 2)
            #     # Convert the byte to its UTF-8 equivalent character and append it to the message
            #     utf8_character = chr(byte_value)
            #     utf8_message += utf8_character
            #     # Check if the end of the message is reached
            #     if utf8_message.endswith("\n\n"):
            #         return utf8_message[:-2]  # Remove the two trailing newline characters
            #     # Remove the first 8 bits from the binary message
            #     binary_message = binary_message[8:]
    return binary_message

# Example usage:
image_path = "/home/ashlerbenda/CovertChannel_DNS/loki_vs_louie_3.png"
binary_message = extract_lsb(image_path)
# Convert binary string to ASCII string
decoded_message = ''.join(chr(int(binary_message[i:i+8], 2)) for i in range(0, len(binary_message), 8))
print(decoded_message)
