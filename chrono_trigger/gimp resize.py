import os, re, json
count = 0
path = r'C:\Users\Morosov\Desktop\Spirites_Sorted\www.videogamesprites.net\ChronoTrigger'
for root, dirs, files in os.walk(path):
    for name in files:
        if ".gif" in name:
            image = pdb.gimp_file_load(root + "\\" + name,root + "\\" + name)                
            x,y = json.loads(os.listdir(root).pop())
            pdb.gimp_image_resize(image,x,y,(-(image.width-x)/2),(-(image.height-y)/2))
            if len(image.layers) > 1:
                delay = int(re.findall(r'(?<=\().*?(?=ms)',str(image.layers[1]))[0])
                pdb.file_gif_save2(image, pdb.gimp_image_get_active_drawable(image), r'file:///' + root + "\\" + name, r'file:///' + root + "\\" + name,0,1,delay,2,1,1,1)
            else:
                pdb.gimp_file_save(image, image.layers[0], root + "\\" + name, '?')