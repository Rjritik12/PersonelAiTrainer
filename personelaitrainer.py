import cv2
import numpy as np
import time
import PoseModule as pm

cap = cv2.VideoCapture("AiTrainer/curls.mp4")
while True:
    success, img = cap.read()
    img = cv2.resize(img, (1280, 720))
    
    img = detector.findPose(img, False)
    lmList = detector.findPosition(img, False)
    
    if len(lmList) !=0:
        
        angle = detector.findAngle(img, 12,14,16)
        
        cv2.rectangle(img, (1100,100), (1175, 658), color, 3)
        cv2.rectangle(img, (1100, int(bar)), (1175, 650), color, 3)
        cv2.putText(img, f'{int(per)}%', (1100, 75), cv2.FONT_HERSHEY-PLAIN, 4, color, 4)
        
        cv2.rectangle(img, (0,450), (250, 720), (0,250,0), cv2.FILLED)
        cv2.putText(img, str(int(count)), (45, 670), cv2.FONT-HERSHEY-PLAIN, 15,(255, 0,0), 25)
    cv2.inshow("Image", img)
    cv2.waitKey(1)
    
    