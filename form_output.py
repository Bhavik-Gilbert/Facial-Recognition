<<<<<<< HEAD
from functions import empty, valid_email, take_picture, remove_local_image, clear_images, create_date, valid_username, clear_empty_record
from functions import face_comparing, convert_binary_data, convert_image, face_detection
from connection import query
import constants

import cv2


def login(username):
    clear_images()

    message = ""

    if(empty(username)):
        message += "Fill in all fields\n"

    if(empty(message)):
        """
        COLLECT SQL IMAGE
        """
        record = (username.capitalize(),)
        select_image = query("""SELECT ImageData, faces.UserID FROM faces 
                                INNER JOIN user
                                ON faces.UserID = user.UserID
                                WHERE user.Username = %s""",  record)

        if(empty(select_image)):
            message = username + " does not exist in the system"
            return message

        if(not take_picture()):
            message = "Error taking image"
            return message
        
        detect = face_detection()
        if not(empty(detect)):
            clear_images()
            return detect

        
        user_id = select_image[0][0]
        image_data = convert_binary_data(constants.check_image_path)

        hit = 0
        miss = 0

        for person in select_image:
            convert_image(person[0], constants.sql_image_path)
            if(face_comparing(constants.sql_image_path,constants.check_image_path)):
                hit += 1    
            else:
                miss += 1

            remove_local_image(constants.sql_image_path)

        clear_images()
        
        if(hit/(hit+miss) > 0.7):
            message = "same"

            record = (user_id, image_data)
            
            query("""
                INSERT INTO
                faces (UserID, ImageData)
                VALUES (%s, %s);
                """,
                record)    
        else:
            message = "You are not " + username + "\nPlease check the details entered and try again"
        

    return message

def signup(username, firstname, surname, email, dob):
    message = ""
    valid = False

    clear_images()

    date_object = create_date(dob)

    if(empty(username) | empty(firstname) | empty(surname) | empty(email) | empty(dob)):
        message += "Fill in all fields\n"
    if(firstname.isnumeric() | surname.isnumeric()):
        message += "Name cannot be numeric\n"
    if not(valid_email(email)):
        message += "Email is invalid\n"
    if(empty(date_object)):
        message += "Date of Birth is invalid\n"
    if(not(valid_username(username))):
        message += username + " is already taken\n"

    if(empty(message)):
        if(not take_picture()):
            message = "Error taking image"
        else:
            clear_empty_record()


            record = (username.capitalize(), firstname.capitalize(), surname.capitalize(), email, date_object)
            query("""
                INSERT INTO
                user (Username, Firstname, Surname, Email, DOB)
                VALUES
                (%s, %s, %s, %s, %s);
                """,
                record)
            
            message = face_detection()

            valid = True

    return message, valid

def confirm_image():
    try:
        """ 
        Select ID from where Image is false
        Upload Image into faces with userID 
        Set Image to true
        """
        record = (False,)
        select_user = query("""SELECT UserID FROM user
                                WHERE Image = %s""", record)
        
        user_id = select_user[0][0] 
        image_data = convert_binary_data(constants.check_image_path)

        record = (user_id, image_data)
        query("""
                INSERT INTO
                faces (UserID, ImageData)
                VALUES
                (%s, %s);
                """,
                record)
        
        record = (True, user_id )
        query("""UPDATE user
                SET Image = %s
                WHERE UserID = %s""", record)
        
        clear_images()

        return True

    except:
        return False

def retake_image():
    clear_images()
    take_picture()

    return face_detection()

def cancel_images():
    clear_images()
    clear_empty_record()
=======
from functions import empty, valid_email, take_picture, remove_local_image, clear_images, create_date, valid_username, clear_empty_record
from functions import face_comparing, convert_binary_data, convert_image, face_detection
from connection import query
import constants

import cv2


def login(username):
    clear_images()

    message = ""

    if(empty(username)):
        message += "Fill in all fields\n"

    if(empty(message)):
        """
        COLLECT SQL IMAGE
        """
        record = (username.capitalize(),)
        select_image = query("""SELECT ImageData, faces.UserID FROM faces 
                                INNER JOIN user
                                ON faces.UserID = user.UserID
                                WHERE user.Username = %s""",  record)

        if(empty(select_image)):
            message = username + " does not exist in the system"
            return message

        if(not take_picture()):
            message = "Error taking image"
            return message
        
        detect = face_detection()
        if not(empty(detect)):
            clear_images()
            return detect

        
        user_id = select_image[0][0]
        image_data = convert_binary_data(constants.check_image_path)

        hit = 0
        miss = 0

        for person in select_image:
            convert_image(person[0], constants.sql_image_path)
            if(face_comparing(constants.sql_image_path,constants.check_image_path)):
                hit += 1    
            else:
                miss += 1

            remove_local_image(constants.sql_image_path)

        clear_images()
        
        if(hit/(hit+miss) > 0.7):
            message = "same"

            record = (user_id, image_data)
            
            query("""
                INSERT INTO
                faces (UserID, ImageData)
                VALUES (%s, %s);
                """,
                record)    
        else:
            message = "You are not " + username + "\nPlease check the details entered and try again"
        

    return message

def signup(username, firstname, surname, email, dob):
    message = ""
    valid = False

    clear_images()

    date_object = create_date(dob)

    if(empty(username) | empty(firstname) | empty(surname) | empty(email) | empty(dob)):
        message += "Fill in all fields\n"
    if(firstname.isnumeric() | surname.isnumeric()):
        message += "Name cannot be numeric\n"
    if not(valid_email(email)):
        message += "Email is invalid\n"
    if(empty(date_object)):
        message += "Date of Birth is invalid\n"
    if(not(valid_username(username))):
        message += username + " is already taken\n"

    if(empty(message)):
        if(not take_picture()):
            message = "Error taking image"
        else:
            clear_empty_record()


            record = (username.capitalize(), firstname.capitalize(), surname.capitalize(), email, date_object)
            query("""
                INSERT INTO
                user (Username, Firstname, Surname, Email, DOB)
                VALUES
                (%s, %s, %s, %s, %s);
                """,
                record)
            
            message = face_detection()

            valid = True

    return message, valid

def confirm_image():
    try:
        """ 
        Select ID from where Image is false
        Upload Image into faces with userID 
        Set Image to true
        """
        record = (False,)
        select_user = query("""SELECT UserID FROM user
                                WHERE Image = %s""", record)
        
        user_id = select_user[0][0] 
        image_data = convert_binary_data(constants.check_image_path)

        record = (user_id, image_data)
        query("""
                INSERT INTO
                faces (UserID, ImageData)
                VALUES
                (%s, %s);
                """,
                record)
        
        record = (True, user_id )
        query("""UPDATE user
                SET Image = %s
                WHERE UserID = %s""", record)
        
        clear_images()

        return True

    except:
        return False

def retake_image():
    clear_images()
    take_picture()

    return face_detection()

def cancel_images():
    clear_images()
    clear_empty_record()
>>>>>>> e33e4c3e5b289d3b579924e9fc6f92ab5e917a8d
