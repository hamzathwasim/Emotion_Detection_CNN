# -*- coding: utf-8 -*-
"""Untitled19.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1OzZN4_BAvbUVBRSV-C3iARooJoXa52cK
"""

import cv2

pip install deepface

from deepface import DeepFace

img = cv2.imread("/content/drive/MyDrive/Emotion Detection/happy kid.jpg")

import matplotlib.pyplot as plt

plt.imshow(img)
plt.axis('off')

plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
plt.axis('off')

predictions = DeepFace.analyze(img)

predictions

type(predictions)

predictions[0]['dominant_emotion'][:]

faceCascade =cv2.CascadeClassifier("/content/drive/MyDrive/Emotion Detection/haarcascade_frontalface_default (1).xml")

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    #detect the faces
faces = faceCascade.detectMultiScale(gray, 1.1, 4)
    #scale factor ,neighbors

    #draw the rectangle around each face
for (x, y, w, h) in faces:
    cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)

plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))

font = cv2.FONT_HERSHEY_SIMPLEX
  #use putText() method for inserting text on video
cv2.putText(img,
                predictions[0]['dominant_emotion'][:],
                (30, 100),
                font, 3,
                (0, 0, 255),
                9,
                cv2.LINE_4) ;

plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))

