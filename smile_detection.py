import cv2
import numpy as np

faceCascade = cv2.CascadeClassifier('haarcascade/haarcascade_frontalface_alt.xml')
eyeCascade = cv2.CascadeClassifier('haarcascade/haarcascade_smile.xml')

capture = cv2.VideoCapture(0, cv2.CAP_DSHOW)
capture.set(3, 640)
capture.set(4, 480)
#img = cv2.imread('Resources/BlackPink.png')
#img = cv2.resize(img, (int(img.shape[1]/2), int(img.shape[0]/2)))
#imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

while True:
    _, img = capture.read()
    imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = faceCascade.detectMultiScale(imgGray, 1.03, 5)

    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)

        roiImg = img[y:y + h, x:x + w]
        roiGray = imgGray[y:y + h, x:x + w]

        eyes = eyeCascade.detectMultiScale(roiGray, 1.8, 9)

        for (ex, ey, ew, eh) in eyes:
            cv2.rectangle(roiImg, (ex, ey), (ex + ew, ey + eh), (0, 255, 0), 2)

    cv2.imshow("img", img)

    if cv2.waitKey(1) &0xff == ord('q'):
       break