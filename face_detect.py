# -*- coding: utf-8 -*-
"""
Created on Wed Dec  1 23:01:36 2021

@author: bskyl
"""

#Kütüphane import etme;
import numpy
import cv2
import pandas as pd
import seaborn as sns
from scipy import ndimage
import cvzone
from cvzone.SelfiSegmentationModule import SelfiSegmentation
import os
import mediapipe as mp 


#Video dosyası okuma;
cap = cv2.VideoCapture(0)
cap.set(3, 640)
cap.set(4, 480)
#frameleri kayıt ettiğimiz dosyamızın adı,
#fileName = "webcam.avi"

codec = cv2.VideoWriter_fourcc('W', 'M', 'V', '2')
#ekran oranı
frameRate = 60
#çözünürlük
resolution = (1080, 1080)

#Art arda while döngüsünde yazdırcağımız frameleri burada dosya haline getireceğiz;
#codec = kod çözücü videoyu doğru bir şekilde kaydetmek için codec değerini girmeliyiz bunlar 4 tane;
#videoFileOutput = cv2.VideoWriter(fileName, codec, frameRate, resolution)
segmentor = SelfiSegmentation()
while True:
    #Frameleri okukoruz burada;
    ret, frame = cap.read()

    #Ayna görüntüsü;
    frame = cv2.flip(frame,1)
    imageOut = segmentor.removeBG(frame, (0,0,0), threshold=0.8)
    img=imageOut
    img=ndimage.rotate(img, 45)
    img=cv2.resize(img,(270,270))
    
    
    img3=ndimage.rotate(img, 90)
    img3=cv2.resize(img3,(270,270))
    
    img4=ndimage.rotate(img, 180)
    img4=cv2.resize(img4,(270,270))
    
    img2=ndimage.rotate(img, -90)
    img2=cv2.resize(img2,(270,270))
    
    a = numpy.vstack((img,img3))
    b = numpy.vstack((img2,img4))
   
   
    horizontalAppendedImg = numpy.hstack((a,b))
    c=ndimage.rotate(horizontalAppendedImg, 45)
    
   

    # Yukarıdaki videoFileOutput'a neyi yazmak istiyoruz frameleri;
    #videoFileOutput.write(c)

    #Webcamde göster diyoruz;
    cv2.imshow("Webcam Live", c)

    # Eğer klavyeden bir değere basarsam ekranı kapat klavye bağlı kod;
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break
#videoları işledikten sonra serbest bırakmalıyız,
#videoFileOutput.release()
cap.release()
cv2.destroyAllWindows()