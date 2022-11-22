#------ External Libraries ------#
import numpy as np
import cv2 
import pywt
import pywt.data
import matplotlib.image as mpimg
import matplotlib.pyplot as plt

CHAR_NUM = 1000 # number of characters
INPUT_IMAGES_PATH = '/Users/sergiorojas/Documents/GitHub/proyecto-piv-puj/data'
OUTPUT_IMAGES_PATH = '/Users/sergiorojas/Documents/GitHub/proyecto-piv-puj/stego_lsb'
TEXT_PATH = '/Users/sergiorojas/Documents/GitHub/proyecto-piv-puj/data.txt'

def run():
    
    original_image_path = INPUT_IMAGES_PATH + '/image0001.png'
    pic = cv2.imread(original_image_path)
    # print(pic[:,:,1].shape)
    
    pic_b = pic[:,:,0]
    # print(pic_b.shape)
    # cA, (cH, cV, cD) = pywt.dwt2(pic_b, 'db3', mode = 'periodization')
    coeffs = pywt.dwt2(pic_b, 'haar', mode='periodization')
    cA, (cH, cV, cD) = coeffs
    print(cA)
    # print(np.uint8(cA))
    # print(cH)
    # print(cV)
    # print(cD)
    cA_int = np.uint8(cA)
    cA_int[1,1] = 60
    coeffsr = np.float32(cA_int), (cH, cV, cD)
    imgr = pywt.idwt2(coeffsr, 'haar', mode='periodization')    
    # print(np.uint8(imgr))

    ncA, (ncH, ncV, ncD) = pywt.dwt2(pic_b, 'haar', mode='periodization')
    print(ncA[1,1])
    print(np.float32(cA_int[1,1]))
    print(np.float32(cA_int))
    print(ncA)
if __name__ == '__main__':
    run()