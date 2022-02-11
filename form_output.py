from functions import empty, valid_email, take_picture, remove_local_image
from functions import face_comparing, convert_binary_data, convert_image
from connection import query


def login(username):
    message = ""
    if(empty(username)):
        message += "Fill in all fields\n"
    if(empty(message)):
        if(not take_picture()):
            message = "Error taking image"
        """
        COLLECT SQL IMAGE
        """
        #record = (username, )
        #select_image = query("""SELECT ImageData, user.UserID FROM faces INNERJOIN user
        #                        ON faces.UserID = user.UserID
        #                        WHERE user.Username = %s,  record)   

        """
        user_id = select_image[0][0]
        image_data = convert_binary_data("person.png")

        hit = 0
        miss = 0

        for person in select_image:
            convert_image(person[0], "sqlimage.png")

            if(face_comparing("sqlimage.png","person.png")):
                hit += 1    
            else:
                miss += 1

            remove_local_image("sqlimage.png")
            remove_local_image()
        """

        """
        if(hit/(hit+miss) > 0.7):
            message = "same"

            #record = (user_id, image_data)
        """
        #   query("""
        #        INSERT INTO
        #        faces (UserID, ImageData)
        #        VALUES
        #        (%s, %s);
        #        """,
        #        record)
        """
        else:
            message = "You are not " + username + "\nPlease check the details entered and try again"
        """

    return message

def signup(username, firstname, surname, email, dob):
    message = ""
    remove_local_image()
    if(empty(username) | empty(firstname) | empty(surname) | empty(email) | empty(dob)):
        message += "Fill in all fields\n"
    if(firstname.isnumeric() | surname.isnumeric()):
        message += "Name cannot be numeric\n"
    if not(valid_email(email)):
        message += "Enter email is invalid\n"
    if(empty(message)):
        if(not take_picture()):
            message = "Error taking image"
        else:
            record = (username, firstname, surname, email, dob)
            query("""
                INSERT INTO
                user (Username, Firstname, Surname, Email, DOB)
                VALUES
                (%s, %s, %s, %s);
                """,
                record)

    return message

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
        image_data = convert_binary_data("person.png")

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
        
        remove_local_image()
    except:
        retake_image()

def retake_image():
    remove_local_image()
    take_picture()
