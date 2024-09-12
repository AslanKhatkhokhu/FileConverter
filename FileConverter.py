'Converter png/jpg/jpeg to WebP'
import sys
import os
import array as arr
from pathlib import Path
import pathlib
from PIL import Image

dir_list = [YOUR PATH]
#Блок пеервірки зображень
for i in dir_list:
    dir = i
    im_path = os.listdir(dir)
    im_list = []
    i = 0
    for i in im_path:
        filename, file_extension = os.path.splitext(dir+i)

        if file_extension == ".jpg" or file_extension == ".jpeg" or file_extension == ".JPG" or file_extension == ".JPEG" or file_extension == ".png" or file_extension == ".PNG" or file_extension == ".gif":
            if file_extension != '':
                print('file extension is correct: ', file_extension)
                im_list.append(filename+file_extension)
                print("+++", im_list)
                continue
            else:
                print('file extension is non correct!: ', filename, ' ', file_extension)
                continue
            continue
        else:
            print('file extension is non correct: ', filename, ' ', file_extension)
            continue
        
#Блок конвертації зображень
    if len(im_list) >= 1:
        for i in im_list:
            file_path, file_extention = os.path.splitext(i)
            output_file = file_path + ".webp"
            if i != output_file:
                try:
                    with Image.open(i) as im:
                        im.save(output_file)
                        os.remove(i)
                except OSError:
                    print("cannot convert ", i)

        print("Convert Sucsessfull! ")
    print('1')
