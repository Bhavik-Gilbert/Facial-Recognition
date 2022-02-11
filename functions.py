""" ------- facial recognition imports -------- """
from __future__ import print_function, unicode_literals
from facepplib import FacePP, exceptions
import emoji

""" ------- tkinter window imports -------- """
import re
from cv2 import VideoCapture, imshow, imread, imwrite, waitKey, destroyWindow
import os




def empty(value):
    try:
        if(len(value)>0):
            return False
        return True
    except:
        return True

def valid_email(email):
    regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'

    if(re.fullmatch(regex, email)):
        return True
    return False

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
        imwrite("person.png", image)
    
        # If keyboard interrupt occurs, destroy image 
        # window
        #waitKey(0)
        #destroyWindow("GeeksForGeeks")

        return True
    # If captured image is corrupted, moving to else part
    else:
        return False

def remove_local_image(filepath:str="person.png"):
    if os.path.exists(filepath):
        os.remove(filepath)
        return True
    else:
        return False


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
    
   
# define global variables
face_detection = ""
faceset_initialize = ""
face_search = ""
face_landmarks = ""
dense_facial_landmarks = ""
face_attributes = ""
beauty_score_and_emotion_recognition = ""
   
# define face comparing function
def face_comparing(image1:str, image2:str):

    # api details
    api_key ='xQLsTmMyqp1L2MIt7M3l0h-cQiy0Dwhl'
    api_secret ='TyBSGw8NBEP9Tbhv_JbQM18mIlorY6-D'
    app = FacePP(api_key = api_key, api_secret = api_secret)
   
    cmp_ = app.compare.get(image_url1 = image1,
                           image_url2 = image2)
   
    # Comparing Photos
    if cmp_.confidence > 70:
        return True
    else:
        return False

          
"""
# Driver Code 
if __name__ == '__main__':
   
    # api details
    api_key ='xQLsTmMyqp1L2MIt7M3l0h-cQiy0Dwhl'
    api_secret ='TyBSGw8NBEP9Tbhv_JbQM18mIlorY6-D'
   
    try:
        # create a logo of app by using iteration,
        # unicode and emoji module-------------
        for i in range(1,6):
              
            for j in range(6,-i):
                print(" " , end = " ")
                  
            for j in range(1,i):
                print('\U0001F600', end =" ")
                  
            for j in range(i,0,-1):
                print('\U0001F6A3', end= " ")
                  
            for j in range(i,1,-2):
                print('\U0001F62B', end= " ")
                  
            print()
              
        print()
       
        for i in range(1,6):
              
            for j in range(6,-i):
                print(" " , end = " ")
                  
            for j in range(1,i):
                print(emoji.emojize(":princess:"), end =" ")
                  
            for j in range(i,0,-1):
                print('\U0001F610', end= " ")
                  
            for j in range(i,1,-2):
                print(emoji.emojize(":baby:"), end= " ")
                  
            print()
           
        # call api
        app_ = FacePP(api_key = api_key, 
                      api_secret = api_secret)
        funcs = [
            face_detection,
            face_comparing_localphoto,
            face_comparing_websitephoto,
            faceset_initialize,
            face_search,
            face_landmarks,
            dense_facial_landmarks,
            face_attributes,
            beauty_score_and_emotion_recognition
        ]
          
        # Pair 1
        image1 = 'Image 1 link'
        image2 = 'Image 2 link'
        face_comparing(app_, image1, image2)
          
        # Pair2
        image1 = 'Image 1 link'
        image2 = 'Image 2 link'
        face_comparing(app_, image1, image2)        
   
    except exceptions.BaseFacePPError as e:
        print('Error:', e)
"""