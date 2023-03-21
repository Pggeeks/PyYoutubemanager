import os
from selenium import webdriver
from chome_debugger_host import Chrome_deb_mode
from XP_conf import *
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

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
        self.driver.implicitly_wait(4)

    def send(self):
        self.driver.get('https://studio.youtube.com/')
        self.driver.find_element(By.XPATH, self.xPath).click()
        try:
            self.driver.find_element(By.XPATH, self.fxPath).send_keys(os.path.normpath(self.file_Path))
        except Exception:
            print('path error retrying')
            self.driver.find_element(By.XPATH, self.fxPath).send_keys(os.path.normpath(self.file_Path))
        self.driver.implicitly_wait(4)

    def Thumbnail(self, Thumb_Path):
        try:
            self.driver.find_element(By.ID, "file-loader").send_keys(Thumb_Path)
        except Exception:
            print('Error, add a proper thumbnail path')

    def details(self, D_Tiltle=None, D_Description=None, prv=False, unl=False):
        def title(title):
            try:
                element = self.driver.find_element(By.ID, "title-textarea")
            except Exception:
                self.driver.implicitly_wait(4)
            element.send_keys(Keys.CONTROL, "a")
            element.send_keys(Keys.DELETE)
            element.send_keys(title)

        def description(des):
            try:
                self.driver.find_element(By.XPATH, XPATH_DESCRIPTION).send_keys(des)
            except Exception:
                pass

        def listed(private, unlisted):
            if private:
                self.driver.find_element(By.NAME, "PRIVATE").click()
            elif unlisted:
                self.driver.find_element(By.NAME, "UNLISTED").click()
            else:
                self.driver.find_element(By.NAME, "PUBLIC").click()

        try:
            if D_Tiltle:
                title(D_Tiltle)
            if D_Description:
                description(D_Description)
        except:
            print('Unable to add title or description, check if you have passed the attributes')
        finally:
            self.driver.implicitly_wait(5)
            try:
                self.driver.find_element(By.NAME, "VIDEO_MADE_FOR_KIDS_NOT_MFK").click()
            except:
                pass
            for _ in range(3):
                self.driver.find_element(By.ID, "next-button").click()
            listed(prv, unl)
            self.driver.find_element(By.ID, "done-button").click()
            print('Video uploaded successfully, you may close this app')
