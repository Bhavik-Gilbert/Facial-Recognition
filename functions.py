""" ------- facial recognition imports -------- """
#METHOD 1
from __future__ import print_function, unicode_literals
from facepplib import FacePP, exceptions
import emoji

#METHOD 2
try:
    from deepface import DeepFace
    import cv2
except:
    pass

#METHOD 3
try:
    import face_recognition
except:
    pass

""" ------- tkinter window imports -------- """
import re
import cv2
from cv2 import VideoCapture, imshow, imread, imwrite, waitKey, destroyWindow, cvtColor
import os
import datetime

from connection import query
import constants


def empty(value):
    try:
        if(len(value)>0):
            return False
        return True
    except:
        return True

def create_date(date):
    try:
        date_list = date.split("/") 
        date_of_birth = datetime.datetime(int(date_list[2]), int(date_list[1]), int(date_list[0])).strftime("%Y,%m,%d")
    except:
        date_of_birth = ""

    return date_of_birth

def valid_email(email):
    regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'

    return (re.fullmatch(regex, email))

def valid_username(username:str):
    record = (username.capitalize(),)
    select_user = query("""SELECT Username FROM user 
                            WHERE Username = %s""",  record)
    
    return empty(select_user)

def detect_faces(path:str=constants.check_image_path):
    casc_path = "haarcascade_frontalface_default.xml"
    face_cascade = cv2.CascadeClassifier(casc_path)
    image = imread(path)
    grey = cvtColor(image, cv2.COLOR_BGR2GRAY)

    faces = face_cascade.detectMultiScale(
        grey,
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(30, 30),
        flags = cv2.CASCADE_SCALE_IMAGE
    )

    return len(faces)

def face_detection(path:str=constants.check_image_path):
    message = ""
    print(path)
    if(detect_faces(path)<1):
        message = "No faces found, it is suggested that you take it again"
            
    if(detect_faces(path)>1):
        message = "Multiple faces found, it is suggested that you take it again"
    
    return message

def take_picture():
    cam_port = 0
    cam = VideoCapture(cam_port)

    result, image = cam.read()
    
    if result:
    
        # showing result, it take frame name and image 
        # output
        #imshow("GeeksForGeeks", image)
    
        # saving image in local storage
        """--- have it add the image to a database in sql ---"""
        imwrite(constants.check_image_path, image)
    
        # If keyboard interrupt occurs, destroy image 
        # window
        #waitKey(0)
        #destroyWindow("GeeksForGeeks")

        return True
    # If captured image is corrupted, moving to else part
    else:
        return False

def remove_local_image(filepath:str=constants.check_image_path):
    if os.path.exists(filepath):
        os.remove(filepath)
        return True
    else:
        return False

def clear_images():
    remove_local_image(constants.sql_image_path)
    remove_local_image()

def clear_empty_record():
    record = (False,)
    query("""
        DELETE FROM user
        WHERE Image = %s""", record)

""" ------- facial recognition -------- """
# Python program for facial comparison

def convert_binary_data(filename):
    # Convert digital data to binary format
    with open(filename, 'rb') as file:
        binaryData = file.read()

    return binaryData

def convert_image(data, filename):
    # Convert binary data to proper format and write it on Hard Disk
    with open(filename, 'wb') as file:
        file.write(data)
   
# define face comparing function
def face_comparing(image1:str, image2:str):
    compare = False
    #METHOD 1
    while True:
        try:
            # api details
            api_key ='xQLsTmMyqp1L2MIt7M3l0h-cQiy0Dwhl'
            api_secret ='TyBSGw8NBEP9Tbhv_JbQM18mIlorY6-D'
            app = FacePP(api_key = api_key, api_secret = api_secret)
        
            cmp_ = app.compare.get(image_url1 = image1,
                                image_url2 = image2)
        
            # Comparing Photos
            if cmp_.confidence > 70:
                compare = True
            break
        except:
            pass
        
        #METHOD 2
        try:
            confirmed_img = cv2.imread('path')
            check_img = cv2.imread('path')

            results = DeepFace.verify(confirmed_img,check_img)
            result = results["verified"]
            if(result):
                compare = True
            break
        except:
            pass

        #METHOD 3
        try:
            confirmed_img = face_recognition.load_image_file('path')
            confirmed_img_encoding = face_recognition.face_encodings(confirmed_img)[0]

            check_img = face_recognition.load_image_file('path')
            check_img_encoding = face_recognition.face_encodings(check_img)[0]

            results = face_recognition.compare_faces([confirmed_img_encoding], check_img_encoding)

            result = results[0]

            if(result):
                compare = True
            break
        except:
            pass

        break
    
    return compare