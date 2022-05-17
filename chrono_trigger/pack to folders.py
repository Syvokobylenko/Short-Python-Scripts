import os, re, shutil
path = r'C:\Users\Morosov\Desktop\Spirites\www.videogamesprites.net\ChronoTrigger'
for root, dirs, files in os.walk(path):
    for name in files:
        try:
            m = re.findall(r'.*?-', name)[0][:-2]
        except(IndexError):
            try:
                m = re.findall(r'.*?\s(?=\()', name)[0][:-1]
            except(IndexError):
                try:
                    m = re.findall(r'.*.gif', name)[0][:-3]
                except(IndexError):
                    print(name + " regex error")
        try:
            os.mkdir(root + "\\" + m)
        except(FileExistsError):
            pass
        shutil.move(root + "\\" + name, root + "\\" + m + "\\" + name)