"""
METHOD 1 - INCOMPLETE

import requests

payload = {"anywhere-upload-input":"Person.jpg"}
r = requests.post("https://imgbb.com/", payload,
        timeout=5)

print(r.text)
"""

"""
METHOD 2

from deepface import DeepFace
import cv2

confirmed_img = cv2.imread('path')
check_img = cv2.imread('path')

results = DeepFace.verify(confirmed_img,check_img)
result = results["verified"]
if(result):
        print("same")
else:
        print("different")
"""

"""
METHOD 3

import face_recognition

confirmed_img = face_recognition.load_image_file('path')
confirmed_img_encoding = face_recognition.face_encodings(confirmed_img)[0]

check_img = face_recognition.load_image_file('path')
check_img_encoding = face_recognition.face_encodings(check_img)[0]

results = face_recognition.compare_faces([confirmed_img_encoding], check_img_encoding)

result = results[0]

if(result):
        print("Same")
else:
        print("Different)
"""