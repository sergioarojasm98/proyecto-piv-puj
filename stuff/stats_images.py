from turtle import width
import cv2
import os

def run():

    # Path for MAC: /Users/sergiorojas/Pictures/ILSVRC/Data/DET/...
    # <test, val, train/ILSVRC2014_train_00XX>
    
    input_images_path = input('Enter files path: ') 
    files_names = os.listdir(input_images_path)

    max_h = 0
    min_h = 9999
    max_w = 0
    min_w = 9999
    avg_h = 0
    avg_w = 0
    
    min_h_path = '<empty>'
    min_w_path = '<empty>'

    total_items = 0 

    for file_name in files_names:
        original_image_path = input_images_path + "/" + file_name
        img = cv2.imread(original_image_path)
        
        height = img.shape[0]
        width = img.shape[1]

        if height > max_h:
            max_h = height

        if height < min_h:
            min_h = height
            min_h_path = original_image_path

        if width > max_w:
            max_w = width

        if width < min_w:
            min_w = width
            min_w_path = original_image_path

        avg_h = avg_h + height
        avg_w = avg_w + width

        total_items += 1

    avg_h = avg_h / total_items
    avg_w = avg_w / total_items

    print('Max. Height: ' + str(max_h))
    print('Max. Width: ' + str(max_w))
    print('Min. Height: ' + str(min_h))
    #print('Path: ' + min_h_path)
    print('Min. Width: ' + str(min_w))
    #print('Path: ' + min_w_path)
    print('Avg. Height: ' + str(avg_h))
    print('Avg. Width: ' + str(avg_w))
    print('Total Items: ' + str(total_items))

if __name__ == '__main__':
    run()