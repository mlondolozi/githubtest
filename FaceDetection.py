import cv2

#this is actually where the training happens 
trained_face_data = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

img = cv2.imread('Nikiwe.jpg')

greyscaled_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

#using the trained data to detect a face of the grey scaled image
face_coordinates = trained_face_data.detectMultiScale(greyscaled_img)
print(face_coordinates)

#draw coordinates on image 
cv2.rectangle(img, (533,373), (533+337,373+337), (255,255,255))
cv2.imshow('Show the selected image', img)
cv2.waitKey()

print('Code Complete!!!')