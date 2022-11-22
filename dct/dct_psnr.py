import os  # built-in
from math import log10, sqrt  # built-in

import cv2  # pip install opencv-python
import matplotlib.pyplot as plt  # pip install -U matplotlib
import numpy as np  # pip install numpy

CHAR_NUM = 10 # number of characters
INPUT_IMAGES_PATH = '/Users/sergiorojas/Documents/GitHub/proyecto-piv-puj/data'
OUTPUT_IMAGES_PATH = '/Users/sergiorojas/Documents/GitHub/proyecto-piv-puj/stego_dct'

def run():

    def psnr(original, compressed):
        mse = np.mean((original - compressed) ** 2)
        if(mse == 0):
            # return random.randint(0,100)
            return 100  
        max_pixel = 255.0
        psnr = 20 * log10(max_pixel / sqrt(mse))
        return psnr

    input_files_names = os.listdir(INPUT_IMAGES_PATH)
    psnr_mean = []
    default_x_ticks = []

    for i in range(CHAR_NUM, CHAR_NUM * 7, CHAR_NUM):
        psnr_list = []
        for input_file_name in input_files_names:
            original = cv2.imread(INPUT_IMAGES_PATH + "/" + input_file_name)
            stego = cv2.imread(OUTPUT_IMAGES_PATH + "/" + input_file_name[:-4] + '_Text' + str(i) + '.png', 1)
            value = psnr(original, stego)
            psnr_list.append(value)
        psnr_mean.append(np.mean(np.array(psnr_list)))
        default_x_ticks.append(i)

    plt.plot(range(len(default_x_ticks)), psnr_mean)
    plt.xticks(range(len(default_x_ticks)), default_x_ticks)
    plt.title('PSNR del Método: DCT')
    plt.xlabel('Número de Caracteres')
    plt.ylim([10, 50])
    plt.ylabel('PSNR (dB)')
    plt.grid()
    plt.show()

if __name__ == "__main__":
    run()