import cv2
import os
from face_detecting import faceDetecting

def getFrame(vidcap, count, sec, name, path):
    # frame image from the video and save
    vidcap.set(cv2.CAP_PROP_POS_MSEC,sec*1000)
    hasFrames,image = vidcap.read()
    if hasFrames:
        detectedFace =  faceDetecting(image)    
        cv2.imwrite(os.path.join(path , name+str(count)+".jpg"), detectedFace)     # save frame as JPG file
    return hasFrames

def videoFraming(videoPath, name):
    # create folder for user's image
    directory = name + '\'s Image'
    path = os.path.join(os.getcwd(), directory)
    if not os.path.exists(path):
        os.makedirs(path)
    ##############
    vidcap = cv2.VideoCapture(videoPath)
    sec = 0
    frameRate =  0.5
    count = 1
    success = getFrame(vidcap, count, sec, name, path)
    while success:
        count = count + 1
        sec = sec + frameRate
        sec = round(sec, 2)
        success = getFrame(vidcap, count, sec, name, path)

name = 'man'
videoPath = 'WIN_20210329_13_46_34_Pro.mp4'

videoFraming(videoPath, name)
