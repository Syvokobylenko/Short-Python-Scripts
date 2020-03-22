import os, random, time
while True:
 wallpaper = "/home/morosov/webm/" + random.choice(os.listdir("/home/morosov/webm/"))
 print(wallpaper)
 lockscreen = "/home/morosov/webm/" + random.choice(os.listdir("/home/morosov/webm/"))
 print(lockscreen)
 try:
  os.remove("/home/morosov/webm/active/wallpaper.webm")
  print("Wallpaper removed.")
 except(FileNotFoundError):
  print("The wallpaper file is missing!")
 try:
  os.remove("/home/morosov/webm/active/lockscreen.webm")
  print("Lock screen removed.")
 except(FileNotFoundError):
  print("The lock screen file is missing!")
 os.popen("cp " + wallpaper + " " + "/home/morosov/webm/active/wallpaper.webm")
 os.popen("cp " + lockscreen + " " + "/home/morosov/webm/active/lockscreen.webm")
 print("Replaced. Wallpaper: " + wallpaper + " Login: " + lockscreen)
 time.sleep(900)