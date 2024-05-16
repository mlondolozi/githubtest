import cv2
from random import randrange

img_file = "CarsPic.jpg"
classifier_file = 'car_detector.xml'

img = cv2.imread(img_file)
black_and_white = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY )

car_tracker = cv2.CascadeClassifier(classifier_file)

cars = car_tracker.detectMultiScale(black_and_white)
print(cars)

for (x,y,w,h) in cars:
    cv2.rectangle(img, (x, y, x+w, y+h), (randrange(255),randrange(255),randrange(255)), 5)

cv2.imshow('Show the selected image', black_and_white)
cv2.waitKey(10000)


print('Code completed')