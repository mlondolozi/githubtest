import cv2
from random import randrange

#this is actually where the training happens 
trained_face_data = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

img = cv2.imread('Nikiwe.jpg')

greyscaled_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

#using the trained data to detect a face of the grey scaled image
face_coordinates = trained_face_data.detectMultiScale(greyscaled_img)
#print(face_coordinates)

#draw coordinates on images for each detect image
for (x,y,w,h) in face_coordinates:
    cv2.rectangle(img, (x, y, x+w, y+h), (randrange(255),randrange(255),randrange(255)), 5)

cv2.imshow('Show the selected image', img)
cv2.waitKey()

print('Code Complete!!!')