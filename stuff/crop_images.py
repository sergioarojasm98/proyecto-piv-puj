import cv2
import os

def run():

    # Path for MAC: /Users/sergiorojas/Pictures/ILSVRC/Data/DET/...
    # <test, val, train/ILSVRC2014_train_00XX>
    
    input_images_path = input('Enter files path: ')
    files_names = os.listdir(input_images_path)

    total_items = 0 

    for file_name in files_names:
        current_image_path = input_images_path + "/" + file_name
        img = cv2.imread(current_image_path)

        y = 0
        x = 0
        h = 360
        w = 480

        crop_img = img[y:h, x:w] 
        cv2.imwrite(current_image_path, crop_img)
        total_items += 1

if __name__ == '__main__':
    run()