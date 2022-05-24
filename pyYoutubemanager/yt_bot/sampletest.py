# before using check the XP_configration file
# please close any chrome browser working .. more in chrome_debugger_host
## This is a Sample Working Of this Program hope you understand..


from download import YTdownload
from uploader import upload

# # this step is for downloading a Youtube video you can skip.. if you have the video locally

a = YTdownload('https://www.youtube.com/watch?v=K4TOrB7at0Y')
fpath = a.Download()   ##fpath gets path of your video when its downloaded
up=upload('path off the') ### pass the absolute path in upload
up.send()
# up.Thumbnail('add the path of thumbnail absolute')
up.details(D_Tiltle='this is title',D_Description='here is the description',Prv=True) 



# ## add title , description
### if you want to publish as Public do not pass anything 