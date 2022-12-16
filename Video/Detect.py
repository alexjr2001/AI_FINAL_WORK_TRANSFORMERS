#Importamos libs
import torch
import cv2
import numpy as np

#Leemos el model    
model=torch.hub.load('ultralytics/yolov5','custom',
path='C:/Users/LENOVO/Documents/AJR/VII SEMESTRE/IA/Video/model/smartwatch.pt')

#Realizamos videoCapture
cap = cv2.VideoCapture(0)

#Empezamos
while True:
    #Lectura 
    ret, frame = cap.read()     ##ERROR: Acá el ret y frame no agarra nada, son false y NONE
    detect = model(frame)

    #Mostramos FPS
    cv2.imshow('Detector de billetes', np.squeeze(detect.render()))

    #Key input  
    t = cv2.waitKey(5)

    if t == 27:
        break

cap.release()
cv2.destroyAllWindows() 
