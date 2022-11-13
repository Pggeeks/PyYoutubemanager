'''
•before using add the CHROMEZ_DRIVER AND CHROMEDEB_PATH Paths..!!!
•if Yotube changes the xpath in the future change the configration here
•Please add double dashes in path
'''
CHROME_DRIVER = "C:\\Users\\docto\\Downloads\\chromedriver_win32\\chromedriver.exe"
## In CHROMEDEB_PATH pass the location of your chrome program file | eg. "C:\\Program Files\\Google\\Chrome\\Application"
CHROMEDEB_PATH = "C:\\Program Files\\Google\\Chrome Beta\\Application"
### all the Xpaths are here and ids are in the main file!
UPLOAD_XPATH = "/html/body/ytcp-app/ytcp-entity-page/div/div/main/div/ytcp-animatable[2]/div[1]/ytcp-quick-actions/a[1]/ytcp-icon-button/tp-yt-iron-icon"

SELECT_FILEX = "/html/body/ytcp-uploads-dialog/tp-yt-paper-dialog/div/ytcp-uploads-file-picker/div/input"
XPATH_DESCRIPTION = '''//div[@aria-label="Tell viewers about your video (type @ to mention a channel)"]'''