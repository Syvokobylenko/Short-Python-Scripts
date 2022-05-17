from PIL import Image, UnidentifiedImageError
import os
count = 0
path = r'C:\Users\Morosov\Desktop\Spirites_Sorted\www.videogamesprites.net\ChronoTrigger'
for root, dirs, files in os.walk(path):
    for name in dirs:
        for sub_root, sub_dirs, sub_files in os.walk(root + "\\" + name):
            current_dimentions = [0,0]
            for sub_name in sub_files:
                try:
                    image = Image.open(sub_root + "\\" + sub_name)
                except (UnidentifiedImageError):
                    continue
                if image.size[0] > current_dimentions[0]:
                    current_dimentions[0] = image.size[0]
                if image.size[1] > current_dimentions[1]:
                    current_dimentions[1] = image.size[1]
            try:
                f = open(sub_root + "\\" + str(current_dimentions), "x")
                f.close()
            except(FileExistsError):
                pass
