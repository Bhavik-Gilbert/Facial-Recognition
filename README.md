# Facial-Recognition
  
### Badges
![GitHub last commit](https://img.shields.io/github/last-commit/Bhavik-Gilbert/Facial-Recognition)
![GitHub contributors](https://img.shields.io/github/contributors/Bhavik-Gilbert/Facial-Recognition)
![Lines of code](https://img.shields.io/tokei/lines/github/Bhavik-Gilbert/Facial-Recognition)
![GitHub repo size](https://img.shields.io/github/repo-size/Bhavik-Gilbert/Facial-Recognition)    

![GitHub top language](https://img.shields.io/github/languages/top/Bhavik-Gilbert/Facial-Recognition)
![GitHub language count](https://img.shields.io/github/languages/count/Bhavik-Gilbert/Facial-Recognition)

## About
This repo contains a basic facial recognition login system where facial biometrics are used in place of traditional passwords. The system strengthens overtime with each
successfull login adding to the bank of facial images used to discern if the user is who they identify to be.
    
## Technologies
### Framworks/Languages
>This application is built using the deepface and tkinter modules in python alongside sql in mysli_connector.
### Hosting
>The application can be run on any device running python 3.7 or later with tkinter, tensorflow, deepface and mysql_connector installed alongside a database setup 
>to hold the recoginition data base on the schema in the repo.
### Installation
>#### Install python 3.7 or above at [python installation](https://www.python.org/downloads/)
>#### Open your terminal and install the following modules using pip
>> pip install tensorflow -> [installation](https://pypi.org/project/tensorflow/)  
>> pip install deepface -> [installation](https://pypi.org/project/deepface/)  
>> pip install tk  -> [installation](https://www.tutorialspoint.com/how-to-install-tkinter-in-python)  
>> pip install mysql-connector  -> [installation](https://pypi.org/project/mysql-connector/)  
>> pip install tkcalendar -> [installation](https://pypi.org/project/tkcalendar/)  
  
  
## Usage
### Getting started
>To use the system, users will first be required to navigate to the signup page  

### Signup
>Users will be required to input some basic details such as name, username and email into a form. Once done, their image will be taken and displayed on screen. The 
user will then be prompted to either upload or retake the photo, repeating the photography process until the user is satisfied and willing to upload their image. The 
image taken is required to have 1 face in it, or the option to upload will not be available, 0 or multiple faces won't be accepted. Along with the image, the rest of 
the data is then sent to the database to be stored.
 
 ### Login
 >To login, users are prompted to type in their username. Once submitted, an image is taken from their camera, which is compared to the various photos currently
 stored for that user. If the user matches, the new photo taken is added to the database, to improve the accuracy of the system, if not, the user is promtpted
 with an error message.
