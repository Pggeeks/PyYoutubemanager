### see the working in sampletest file !!###
import os
from pydoc import text
from selenium import webdriver
from chome_debugger_host import Chrome_deb_mode
from XP_conf import *
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

class upload:
    def __init__(self, file_Path, xPath=UPLOAD_XPATH, fxPath=SELECT_FILEX, option=True):
        self.xPath = xPath
        self.file_Path = file_Path
        self.fxPath = fxPath
        s = Service(CHROME_DRIVER)
        if option:
            self.options = Chrome_deb_mode()  # open chrome in debugger state ,
            # if you want to disable just pass option = False
            self.driver = webdriver.Chrome(service=s, options=self.options)
        else:
            self.driver = webdriver.Chrome(service=s)
    def send(self):
        self.driver.get('https://studio.youtube.com/')
        self.driver.find_element(By.XPATH, self.xPath).click()
        self.driver.implicitly_wait(4)
        try:
            self.driver.find_element(
                By.XPATH, self.fxPath).send_keys(f"{self.file_Path}")
            self.driver.implicitly_wait(4)
        except:
            print('path error retrying')
            # if the path have forward or backslash problems it will correct it as per the system
            abb = os.path.normpath(self.file_Path)
            self.driver.find_element(
                By.XPATH, self.fxPath).send_keys(f"{abb}")
            self.driver.implicitly_wait(4)
    # adds thumbnail to video !! run it before details function

    def Thumbnail(self, Thumb_Path):
        try:
            self.driver.implicitly_wait(10)
            self.driver.find_element(By.ID, "file-loader").send_keys(Thumb_Path)
        except:
            print('Error ,Add a proper thumbnail path')

###  nested fuction for Details ie. title , description, listed type ###
    def details(self, D_Tiltle=None, D_Description=None, Prv=False, Unl=False):
        def Title(title):
            try:
                self.driver.implicitly_wait(4)
                self.driver.find_element(
                    By.ID, "title-textarea").send_keys(title)
            except:
                self.driver.implicitly_wait(5)
                self.driver.find_element(
                    By.ID, "title-textarea").send_keys(title)

        def Description(des):
            try:
                self.driver.implicitly_wait(4)
                text_element =self.driver.find_element(By.XPATH, XPATH_DESCRIPTION).send_keys(des)
                
            except:
                self.driver.implicitly_wait(5)
                self.driver.find_element(
                    By.XPATH, XPATH_DESCRIPTION).send_keys(des)

        def Listed(Private, Unlisted):
            if Private:
                self.driver.find_element(By.NAME, "PRIVATE").click()
            elif Unlisted:
                self.driver.find_element(By.NAME, "UNLISTED").click()
            else:
                self.driver.find_element(By.NAME, "PUBLIC").click()
        try:
            if D_Tiltle:
                Title(D_Tiltle)  # calls Title function
            if D_Description:
                Description(D_Description)  # calls description function
        except:
            print('unable to add title or description check if you have passed the attributes')
        finally:
            self.driver.implicitly_wait(5)
            # clicks the not made for kids btn.
            try:
                self.driver.find_element(By.NAME, "VIDEO_MADE_FOR_KIDS_NOT_MFK").click()
            except:
                self.driver.find_element(By.NAME, "VIDEO_MADE_FOR_KIDS_NOT_MFK").click()        
            for _ in range(3):
                self.driver.implicitly_wait(4)
                self.driver.find_element(By.ID, "next-button").click()
            # calls listed function for private , unlisted else public
            Listed(Prv, Unl)
            # click the last submit btn
            self.driver.find_element(By.ID, "done-button").click()

### nested function ends here. ###
