# RGB values extracted from the PNG file
rgb_values = [
    194, 131, 173, 131, 57, 116, 147, 42, 147, 153, 8, 156, 152, 0, 152, 147,
    0, 149, 146, 0, 150, 145, 0, 150, 134, 0, 141, 124, 0, 130, 125, 0, 130,
    148, 0, 153, 154, 0, 155, 146, 5, 148, 132, 0, 134, 114, 0, 114, 91, 0,
    93, 69, 0, 69, 77, 0, 77, 94, 0, 93, 117, 0, 117, 126
]

# Extract LSB of each RGB value and concatenate them into a binary string
binary_string = ''.join(str(rgb & 1) for rgb in rgb_values)

# Convert binary string to ASCII
ascii_string = ''.join(chr(int(binary_string[i:i+8], 2)) for i in range(0, len(binary_string), 8))

print(ascii_string)
