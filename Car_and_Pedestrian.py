import cv2

img_file = "CarPic.jpg"
classifier_file = 'car_detector.xml'

img = cv2.imread(img_file)

car_tracker = cv2.CascadeClassifier(classifier_file)

print('Code completed')