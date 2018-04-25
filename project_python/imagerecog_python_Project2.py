# -*- coding: utf-8 -*-
"""
Created on Tue Apr 24 00:48:14 2018

@author: Kasutaja
"""

import cv2
import matplotlib.pyplot as plt



def convertToRGB(img):
    return cv2.cvtColor(img, cv2.COLOR_BGR2RGB)


#load cascade classifier training file for haarcascade
haar_face_cascade = cv2.CascadeClassifier('C:\\Users\\Kasutaja\\Documents\\python_class_project\\haarcascade_frontalface_alt.xml')




def detect_faces(f_cascade, colored_img, scaleFactor = 1.5):
    #just making a copy of image passed, so that passed image is not changed
    img_copy = colored_img.copy()
    
    #convert the test image to gray image as opencv face detector expects gray images
    gray = cv2.cvtColor(img_copy, cv2.COLOR_BGR2GRAY)
    
    #let's detect multiscale (some images may be closer to camera than others) images
    faces = f_cascade.detectMultiScale(gray, scaleFactor=scaleFactor, minNeighbors=5);
    
    #go over list of faces and draw them as rectangles on original colored img
    for (x, y, w, h) in faces:
        cv2.rectangle(img_copy, (x, y), (x+w, y+h), (0, 255, 0), 2)
        
    return img_copy


#load another image
test2 = cv2.imread('C:\\Users\\Kasutaja\\Pictures\\Saved Pictures\\elonMusk.jpg')

#call our function to detect faces
faces_detected_img = detect_faces(haar_face_cascade, test2)

#conver image to RGB and show image
plt.imshow(convertToRGB(faces_detected_img))