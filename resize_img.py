import cv2
from file_helpers import *
from tkinter.filedialog import askopenfilenames
import os

# general function that returns user input when valid_func returns true (with the input as an argument)
# valid_func is a function that reuturns true or false
def query_loop(message_str: str, err_str: str, valid_func):
    while True:

        res = input(message_str)
        if valid_func(res):
            return res

        print(err_str)

# resize an image to the set size while maintaining aspect ratio
def main():

    files = askopenfilenames(title='Select images to resize')  # show dialog box

    # get the new image sizes
    is_num = lambda s: True if s.isdigit() or s == "" else False
    resize_x = int(query_loop("Enter new x dimension: ", "Please enter an integer", is_num))

    for file in files:
        # only for jpg and png
        if check_extension(file).lower() == 'jpg' or check_extension(file).lower() == 'png':

            # load image including colour and alpha
            img = cv2.imread(file, cv2.IMREAD_UNCHANGED)

            height = img.shape[0]
            width = img.shape[1]

            # get y size from ratio
            resize_y = int(height*(resize_x/width))

            print(f'New Size: {resize_x}x{resize_y}')
            # resize image to (dimensions) by a factor (fx/fy) of 0.5
            img = cv2.resize(img, (resize_x, resize_y))

            # get path to directory
            dir_path = get_path(file)

            # get output name
            out_name = get_filename_from_path(file)
            print(f'Saving file \'resize_{out_name}\' ')

            new_fname = os.path.join(dir_path, 'resize_'+out_name)

            cv2.imwrite(new_fname, img)

if __name__ == "__main__":
    main()