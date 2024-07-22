######################################################################################################################
# Import statement
######################################################################################################################
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep
import time
import csv

######################################################################################################################
#   Function Name   :   read_credentials
#   Input           :   File path .csv File
#   Output          :   Username,Password
#   Description     :   Get the username password from csv file
#   Author          :   Rushikesh Hemant Gholap
#   Date/Time       :   22/07/2024 01:33 pm
######################################################################################################################
def read_credentials(csv_filename):

    OpenFile = open(csv_filename, mode='r')
    csv_reader = csv.DictReader(OpenFile)
    for row in csv_reader:
        username = row['username']
        password = row['password']

    return username, password

######################################################################################################################
#   Function Name   :   Instagram_Login
#   Input           :   String(Username, Password)
#   Output          :    -
#   Description     :   this function perform automation to login instagram
#   Author          :   Rushikesh Hemant Gholap
#   Date/Time       :   22/07/2024 01:33 pm
######################################################################################################################
def Instagram_Login(Username, Password):

    Driver = webdriver.Chrome()
    Driver.get('https://www.instagram.com/')
    sleep(4)
    User_Name = Driver.find_element(By.NAME, 'username')
    User_Name.send_keys(Username)

    User_Name = Driver.find_element(By.NAME, 'password')
    User_Name.send_keys(Password)

    Login_Button = Driver.find_element(
        By.XPATH, '//*[@id="loginForm"]/div/div[3]')
    Login_Button.click()
    sleep(15)

    not_now_button = Driver.find_element(
        By.XPATH, "//button[contains(text(), 'Not Now')]")
    not_now_button.click()
    sleep(30)

    Driver.quit()

######################################################################################################################
#   Function Name   :   Facebook_login
#   Input           :   String(Username, Password)
#   Output          :    -
#   Description     :   this function perform automation to login facebook
#   Author          :   Rushikesh Hemant Gholap
#   Date/Time       :   22/07/2024 01:33 pm
######################################################################################################################
def Facebook_login(Username, Password):

    Driver = webdriver.Chrome()
    Driver.get('https://www.facebook.com/login/')

    Facebook_Username = Driver.find_element(By.NAME, 'email')
    Facebook_Username.send_keys(Username)
    Facebook_password = Driver.find_element(By.NAME, 'pass')
    Facebook_password.send_keys(Password)
    sleep(4)
    
    button = Driver.find_element(By.NAME, value="login")
    button.click()
    sleep(20)
    
    Driver.quit()

######################################################################################################################
#   Function Name   :   Whatsapp_Login
#   Input           :   String(Mobile number)
#   Output          :    -
#   Description     :   this function perform automation to login whatsapp
#   Author          :   Rushikesh Hemant Gholap
#   Date/Time       :   22/07/2024 01:33 pm
######################################################################################################################
def Whatsapp_Login(MobileNumber):

    Driver = webdriver.Chrome()
    Driver.get('https://web.whatsapp.com/')
    sleep(10)

    Button = Driver.find_element(
        By.XPATH, '//*[@id="app"]/div/div[2]/div[3]/div[1]/div/div/div[3]/div/span')
    Button.click()
    sleep(8)

    Text = Driver.find_element(
        By.XPATH, '//*[@id="app"]/div/div[2]/div[3]/div[1]/div/div[3]/div[1]/div[2]/div/div/div/form/input')
    Text.send_keys(MobileNumber)
    sleep(8)

    Next = Driver.find_element(
        By.XPATH, '//*[@id="app"]/div/div[2]/div[3]/div[1]/div/div[3]/div[2]/button/div/div')
    Next.click()
    sleep(30)

    Driver.quit()
    
######################################################################################################################
#   Function Name   :   Youtube_Open
#   Input           :   String(Song name)
#   Output          :    -
#   Description     :   this function perform automation to open youtube and play
#                       the song
#   Author          :   Rushikesh Hemant Gholap
#   Date/Time       :   22/07/2024 01:33 pm
######################################################################################################################
def Youtube_Open(Song):

    Driver = webdriver.Chrome()
    Driver.get(
        'https://www.google.com/webhp?hl=en&sa=X&ved=0ahUKEwi23Oy2vbiHAxXRyDgGHa46AmwQPAgI')
    sleep(4)

    Search = Driver.find_element(By.NAME, "q")
    Search.send_keys('Youtube')

    Enter = Driver.find_element(By.NAME, "q").send_keys("\ue007")
    sleep(6)

    YouTube_Home = Driver.find_element(
        By.XPATH, '//*[@id="rso"]/div[1]/div/div/div/div/div/div/div/div[1]/div/span/a/h3')
    YouTube_Home.click()
    sleep(4)

    Search_Query = Driver.find_element(By.NAME, "search_query")
    Search_Query.send_keys(Song)
    sleep(4)

    Enter = Driver.find_element(By.NAME, "search_query")
    Enter.send_keys("\ue007")
    sleep(6)

    Driver.find_element(
        By.XPATH, '//*[@id="thumbnail"]/yt-image/img').click()
    sleep(60)

    Driver.quit()

######################################################################################################################
#   Entery Point Function
######################################################################################################################
def main():

    print("!------------------------------ Welcome to Automation Script -------------------------------!")
    
    while (True):

        print("Display Automation script ")
        print("Press 1 for : Instagram Login")
        print("Press 2 for : Whatsapp Login")
        print("Press 3 for : Facebook Login")
        print("Press 4 for : Youtube Open")
        print("Press 5 for : Exit from script")

        print("Enter the Number :", end="")
        Num = int(input())

        if (Num != 5):
            print("---------------------------------")

        match Num:

            case 1:
                try:
                    csv_filename = 'Instagram.csv'
                    UserName, PassWord = read_credentials(csv_filename)
                    Starttime = time.time()
                    Instagram_Login(UserName, PassWord)
                    Endtime = time.time()
                    print("Time to execute for this :",Starttime-Endtime)
                except Exception as error:
                    print("Exception for :" ,error)     

            case 2:
                print("Enter your whatsapp No :", end="")
                Mobile = str(input())
                if (len(Mobile) == 10):
                    try:
                        Starttime = time.time()
                        Whatsapp_Login(Mobile)
                        Endtime = time.time()
                        print("Time to execute for this :",Starttime-Endtime)
                    except Exception as error:
                        print("Exception for :" ,error)     
                else:
                    print("Check the phone number......")
                    print("---------------------------------")

            case 3:
                try:
                    csv_filename = 'Facebook.csv'
                    UserName, PassWord = read_credentials(csv_filename)
                    Starttime = time.time()
                    Facebook_login(UserName,PassWord)
                    Endtime = time.time()
                    print("Time to execute for this :",Starttime-Endtime)
                except Exception as error:
                    print("Exception for :" ,error)     
                     
            case 4:
                print("Which song you want to listen :",end="")
                Song = str(input())
                try:
                    Starttime = time.time()
                    Youtube_Open(Song)
                    Endtime = time.time()
                    print("Time to execute for this :",Starttime-Endtime)
                except Exception as error:
                    print("Exception for :" ,error)     
                   
            case 5:
                print("!---------------------------- Thanks for using Automation script ---------------------------!")
                exit()
                
                
######################################################################################################################
#   Starter
######################################################################################################################
if (__name__ == "__main__"):
    main()
