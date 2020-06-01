'''
Github Id: shantanugupta1118
Programmer: Shantanu Gupta (PSIT B.Tech - CSE, (Second year))
'''


import cv2
import sys

face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
video_capture = cv2.VideoCapture(0)
                            # use '0'  ---> main inbuilt camera
                        #    use '1' ----> external or secondary camera 
                            
while True:
    #capture frame by frame
    return_value, frame = video_capture.read()
    
    
    #convert them into grayScale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    faces = face_cascade.detectMultiScale(
        gray,
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(35, 35)
    ) 
    #width = 35, height = 35 --> 35x35
    
    #Draw a rectangle around recognized face
    for (x,y,w,h) in faces:
        cv2.rectangle(frame, (x,y), (x+w, y+h), (50,50,200),2)
        
    #display the result
    cv2.imshow('Face Detection', frame)
    
    #exit the camera
    if cv2.waitKey(1) & 0xFF == ord('q'):
        sys.exit()
    