# Reference: https://github.com/rroy1212/Image_Steganography/blob/master/ImageSteganography.ipynb

#------ External Libraries ------#
import os  # built-in
from math import log10, sqrt  # built-in

import cv2  # pip install opencv-python
import matplotlib.pyplot as plt  # pip install -U matplotlib
import numpy as np  # pip install numpy

#================================#

CHAR_NUM = 1000 # number of characters
INPUT_IMAGES_PATH = '/Users/sergiorojas/Documents/GitHub/proyecto-piv-puj/data'
OUTPUT_IMAGES_PATH = '/Users/sergiorojas/Documents/GitHub/proyecto-piv-puj/stego_lsb'
TEXT_PATH = '/Users/sergiorojas/Documents/GitHub/proyecto-piv-puj/data.txt'

# ============================================================================= #
# ============================================================================= #
# =========================== BEGIN CODE OPERATION ============================ #
# ============================================================================= #
# ============================================================================= #

def run():

    def message_to_binary(message):
        if type(message) == str:

            # ord function returns an integer representing the Unicode character
            # the Unicode Standard classifies 1,481 characters as belonging to the Latin script
            # link: https://en.wikipedia.org/wiki/List_of_Unicode_characters

            return ''.join([format(ord(i), '08b') for i in message]) # string.join(iterable) -> list comprehension
        elif type(message) == bytes or type(message) == np.ndarray:
            return [format(i, '08b') for i in message]
        elif type(message) == int or type(message) == np.uint8:
            return format(message, '08b')
        else:
            raise TypeError('Input type not supported')

    def hide_message(image, secret_message):

        # the maximum bytes to encode: ( wight * height * 3 RGB arrays ) / 8 bits per character
        # however, I could use 7 bits per character since I'm only using english text
        # which means that the max. Unicode character would be the integer 126 that is 1111110

        n_bytes = image.shape[0] * image.shape[1] * 3 // 8 # --> ( 360 px * 480 px * 3 ) / 8 =  64800
        if len(secret_message) > n_bytes:
            raise ValueError('Error encountered insufficient bytes, need bigger image or less data')
        secret_message += '[END]' # you can use any string as the delimeter
        data_index = 0
        # it converts input data to binary format using message_to_binary()
        binary_secret_message = message_to_binary(secret_message)
        data_length = len(binary_secret_message) # to find the length of data that needs to be hidden
        
        for values in image:
            for pixel in values:
                # in the case of color images, the decoded images will have the channels stored in BGR order
                # link: https://docs.opencv.org/3.4/d4/da8/group__imgcodecs.html
                b, g, r = message_to_binary(pixel)
                # modify the least significant bit only if there is still data to store
                if data_index < data_length:
                    # hide the data into least significant bit of red pixel
                    pixel[0] = int(b[:-1] + binary_secret_message[data_index], 2)
                    data_index += 1
                if data_index < data_length:
                    # hide the data into least significant bit of green pixel
                    pixel[1] = int(g[:-1] + binary_secret_message[data_index], 2)
                    data_index += 1
                if data_index < data_length:
                    # hide the data into least significant bit of  blue pixel
                    pixel[2] = int(r[:-1] + binary_secret_message[data_index], 2)
                    data_index += 1
                # if data is encoded, just break out of the loop
                if data_index >= data_length:
                    break

        return image

    input_files_names = os.listdir(INPUT_IMAGES_PATH)

    for i in range(CHAR_NUM, CHAR_NUM * 66, CHAR_NUM):
        if i == 65000:
            with open(TEXT_PATH, 'r') as file:
                message = file.read(64800).rstrip() # rstrip removes spaces at the end of the string
            for input_file_name in input_files_names:
                original_image_path = INPUT_IMAGES_PATH + '/' + input_file_name 
                stego_image_name = input_file_name[:-4] + '_Text' + str(64800) + '.png' # 
                pic = cv2.imread(original_image_path)
                os.chdir(OUTPUT_IMAGES_PATH)
                cv2.imwrite(stego_image_name, hide_message(pic, message))
        else:
            with open(TEXT_PATH, 'r') as file:
                message = file.read(i).rstrip() # rstrip removes spaces at the end of the string
            for input_file_name in input_files_names:
                original_image_path = INPUT_IMAGES_PATH + '/' + input_file_name 
                stego_image_name = input_file_name[:-4] + '_Text' + str(i) + '.png'
                pic = cv2.imread(original_image_path)
                os.chdir(OUTPUT_IMAGES_PATH)
                cv2.imwrite(stego_image_name, hide_message(pic, message))

if __name__ == '__main__':
    run()