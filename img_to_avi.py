import os
import cv2
import numpy as np


path = "/home/zheng/image/200/img/"  # 替换路径

filelist = os.listdir(path)
filelist.sort()

fps = 55
size = (640, 480)
video = cv2.VideoWriter("img_200.avi", cv2.VideoWriter_fourcc('I', '4', '2', '0'), fps, size)


for item in filelist:
    if item.endswith('.jpg'): 
        item = path + item
        img = cv2.imread(item)
        video.write(img)
        

video.release()
