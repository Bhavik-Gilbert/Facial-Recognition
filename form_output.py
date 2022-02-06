from email import message
from functions import empty, valid_email, take_picture, remove_local_image


def login(firstname, surname):
    message = ""
    if(empty(firstname) | empty(surname)):
        message += "Fill in all fields\n"
    if(firstname.isnumeric() | surname.isnumeric()):
        message += "Name cannot be numeric\n"
    if(empty(message)):
        message = "Success"

    return message

def signup(firstname, surname, email, dob):
    message = ""
    remove_local_image()
    if(empty(firstname) | empty(surname) | empty(email) | empty(dob)):
        message += "Fill in all fields\n"
    if(firstname.isnumeric() | surname.isnumeric()):
        message += "Name cannot be numeric\n"
    if not(valid_email(email)):
        message += "Enter email is invalid\n"
    if(empty(message) & (not take_picture())):
            message = "Error taking image"

    return message

def confirm_image():
    remove_local_image()

def retake_image():
    remove_local_image()
    take_picture()
