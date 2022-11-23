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

        height = img.shape[0]
        width = img.shape[1]

        if (height >= 360) and (width >= 480):
            total_items += 1
        else:
            # print(img.shape)
            os.remove(current_image_path)

    print(total_items)

if __name__ == '__main__':
    run()