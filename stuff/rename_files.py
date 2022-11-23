import os

def run():
    
    # Path for MAC: /Users/sergiorojas/Pictures/ILSVRC/Data/DET/...
    # <test, val, train/ILSVRC2014_train_00XX>
    
    input_images_path = input('Enter files path: ')
    files_names = os.listdir(input_images_path)

    aux_1 = 1
    for file_name in files_names:
        original_image_path = input_images_path + "/" + file_name
        os.rename(original_image_path, input_images_path + "/Original_" + str(aux_1) + ".JPEG")
        aux_1 += 1

if __name__ == '__main__':
    run()