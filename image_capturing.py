import cv2
import os
def capturing(video_path):
    substring = video_path.split('.',1)
    dir = substring[0]
    #print(dir)
    parent = 'C:/Users/91936/Desktop/CIP(ambulance)/'
    path = os.path.join(parent,dir)
    os.mkdir(path)
    #print(path)
    photo_path = path + '/'
    vidcap = cv2.VideoCapture(video_path)
    def getFrame(sec):
        vidcap.set(cv2.CAP_PROP_POS_MSEC,sec*1000)
        hasFrames,image = vidcap.read()
        if hasFrames:
            cv2.imwrite(photo_path + str(count)+".jpg", image)
        return hasFrames
    sec = 0
    frameRate = 5 
    count=1
    success = getFrame(sec)
    while success:
        count = count + 1
        sec = sec + frameRate
        sec = round(sec, 2)
        success = getFrame(sec)
    return photo_path
