import cv2
import numpy as np 
import math
import time
import mediapipe as mp
import cvzone

from cvzone.HandTrackingModule import HandDetector

cap = cv2.VideoCapture(0)

detector = HandDetector(detectionCon=0.7, maxHands=2)
ptime = 0
while True:
    success, img = cap.read()
    hands, img = detector.findHands(img)
    fingers=[0,0,0,0,0]
    if hands:
        hand1 = hands[0]
        lmList1 = hand1["lmList"]
        # you can use the bleow code to get the x and y coordinates of the landmarks

        x4, y4 = lmList1[4][0], lmList1[4][1]
        x2, y2 = lmList1[2][0], lmList1[2][1]
        if x2 >= x4:
            fingers[0] = 1
        x8, y8 = lmList1[8][0], lmList1[8][1]
        x6, y6 = lmList1[6][0], lmList1[6][1]
        if y8 <= y6:
            fingers[1] = 1

        x12, y12 = lmList1[12][0], lmList1[12][1]
        x10, y10 = lmList1[10][0], lmList1[10][1]
        if y12 <= y10:
            fingers[2] = 1
        x16, y16 = lmList1[16][0], lmList1[16][1]
        x14, y14 = lmList1[14][0], lmList1[14][1]
        if y16 <= y14:
            fingers[3] = 1
        x20, y20 = lmList1[20][0], lmList1[20][1]
        x18, y18 = lmList1[18][0], lmList1[18][1]
        if y20 <= y18:
            fingers[4] = 1
        
        print(sum(fingers))

            # >or you can use the above 
        # fingers = detector.fingersUp(hand1)

        cv2.rectangle(img, (20, 225), (170, 425), (0, 255, 0), cv2.FILLED)
        cv2.putText(img, str(sum(fingers)), (45, 375), cv2.FONT_HERSHEY_PLAIN, 10, (255, 0, 0), 25)


    ctime = time.time()
    fps = 1/(ctime - ptime)
    ptime = ctime
    cv2.putText(img, f'FPS: {int(fps)}', (40, 50), cv2.FONT_HERSHEY_PLAIN, 3, (255, 0, 0), 3)
    cv2.imshow("Image", img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

