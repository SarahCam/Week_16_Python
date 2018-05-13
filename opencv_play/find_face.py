import cv2
import numpy

#Holds model of what looks like a face
face_cascade = cv2.CascadeClassifier("./.env/lib/python3.6/site-packages/cv2/data/haarcascade_frontalface_default.xml")

img = cv2.imread("emily.JPG")

#convert to greyscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# cv2.imwrite("emily_gray.jpg", gray)

# if find face... pull it out
faces = face_cascade.detectMultiScale(gray, 1.3, 5)

# draw rectangle round each face...
if(len(faces) > 0):
    for (x, y, w, h) in faces:
        gray = cv2.rectangle(gray, (x,y), (x+w, y+h), (0,0,255), 2)
        cv2.imwrite("face.jpg", gray)
