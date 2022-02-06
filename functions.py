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

def remove_local_image():
    if os.path.exists("person.png"):
        os.remove("person.png")
        return True
    else:
        return False