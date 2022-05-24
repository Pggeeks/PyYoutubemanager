### see the working in sampletest file !!###
# close any other chrome browser working because this file opens chrome in your looged in session
# at the localhost which will interfare the working
# opens  chrome in debugger mode by default
# pass option = False in upload to disable it
import os
from threading import Thread
from XP_conf import CHROMEDEB_PATH
from selenium.webdriver.chrome.options import Options
CHROME_PATH = CHROMEDEB_PATH


class chrome_Run:
    def __init__(self, chrome_Path=CHROME_PATH):
        self.chrm_path = chrome_Path

    def cmdline(self):
        os.chdir(self.chrm_path)
        os.system("chrome.exe --remote-debugging-port=9222")

# runs


def Chrome_deb_mode():
    new_thread = Thread(target=chrome_Run().cmdline)  # runs cmdline function
    new_thread.start()
    opt = Options()
    # for opening window in chrome localhost
    opt.add_experimental_option("debuggerAddress", "localhost:9222")
    return opt  # returns option data to upload
