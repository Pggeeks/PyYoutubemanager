from download import YTdownload
from uploader import upload
from reddownloder import Download
import os
class cmdline_uploder:
    def inputtaker(self):
        inputdata = input('do you want to download a yt video for reupload !! Press Y/N and N for local upload \n').lower()
        if inputdata == "y":
            inputype = input('Download from Reddit/Youtube press R/Y :-\n').lower()
            if inputype=='y':
                videolink=input('paste the link here! \n')
                a = YTdownload(str(videolink))
                videopath = a.Download()
                self.info(videopath)
            elif inputype=='r':
                rl=input('paste the link here! \n')
                Download(rl,destination=os.getcwd())
                self.info(os.getcwd()+'\Redditdownloaded.mp4')

            ############################
        elif inputdata == "n":
            videopath = input('paste the absolute video path \n')
            self.info(videopath)
        else:
            print('select a appropriate option')
            self.inputtaker()

    def info(self,videoadd):
        upload_obj = upload(videoadd)
        upload_obj.send()
        thumbnail_or_not =input('wanna add a thumbnail? press Y/N \n').lower()
        if thumbnail_or_not == "y":
            thumbpath =input('paste the thumbnail absolute path \n')
            upload_obj.Thumbnail(str(thumbpath))
        Title = input(' Add a Video Title \n')
        Clip_Credit = input('Add a Clip Credit \n')
        des = open(os.path.dirname(__file__) + '/../mydescription.txt','r',encoding='UTF-8').readlines()
        Data_Des = ''
        for Line in des:
            if 'Credits' in Line:
                Line = Line.rstrip()
                Line = Line.replace(Line, f"{Line}{Clip_Credit}\n")
            Data_Des += Line
        upload_obj.details(D_Tiltle=Title,D_Description=Data_Des)
if __name__ == "__main__":
    cmdline_uploder().inputtaker()
