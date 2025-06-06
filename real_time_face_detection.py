
import numpy as np 
import cv2


face_cascade = cv2.CascadeClassifier('./model/haarcascade_frontalface_default.xml') #loading a trained Viola–Jones detector


def face_detection(img):
    
    image = img.copy()
    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    
    box,detections=face_cascade.detectMultiScale2(img_gray,minNeighbors=8) #detecting faces in a grayscale image using a Haar cascade
    
    
    for x,y,w,h in box:
        cv2.rectangle(image,(x,y),(x+w,y+h),(0,255,0),6) #TOP LEFT CORNER AND BOTTOM RIGHT CORNER OF THE FACE
    
    return image

# %%
cap = cv2.VideoCapture(0) 
while True:
    ret, frame = cap.read() 
    if ret == False:
        break
    img_detect = face_detection(frame)
    cv2.imshow('real time face detection', img_detect)
    if cv2.waitKey(1) == ord('q'):
        break 

cap.release()
cap.destroyAllWindows()



