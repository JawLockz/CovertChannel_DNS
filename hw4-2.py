import numpy as np
import PIL.Image

def decode_message(fname):
    image = PIL.Image.open(fname, 'r')
    image_arr = np.array(list(image.getdata()))

    if image.mode == "P":
        print("Image mode not supported")
        return None

    channels = 4 if image.mode == "RGBA" else 3

    pixels = image_arr.size // channels

    bit_message = ""

    index = 0
    
    for i in range(pixels):
        for j in range(0,3):
            bit_message += bin(image_arr[i][j])[-1]  # Extract the LSB of each pixel value
            index += 1
            if(bit_message.endswith("0010010000110100001100110011011000100100")):
                decoded_message = "".join(chr(int(bit_message[i:i+8], 2)) for i in range(0, len(bit_message), 8))
                return decoded_message
   
    decoded_message = "".join(chr(int(bit_message[i:i+8], 2)) for i in range(0, len(bit_message), 8))
    return decoded_message

image_file = "/home/ashlerbenda/CovertChannel_DNS/loki_vs_louie_3.png"
decoded_message = decode_message(image_file)
if decoded_message:
    print("Decoded message:")
    print(decoded_message)
