import typer
from download import YTdownload
from uploader import upload
from reddownloder import Download
import os
app = typer.Typer(add_completion=False,
    help='''
    ############################################################################
    • Welcome To Youtube Manager New To The App Check XP_conf.py File First\n 
    • Upload Videos to Youtube With Description,Title,Credits,Thumbnail Of your own Choice and much more. \n 
    • Download Them From Various Sources\n
    ############################################################################
    '''
    )

def info(videoadd):
    upload_obj = upload(videoadd)
    upload_obj.send()
    thumbnail_or_not = input('wanna add a thumbnail? press Y/N \n').lower()
    if thumbnail_or_not == "y":
        thumbpath = input('paste the thumbnail absolute path \n')
        upload_obj.Thumbnail(str(thumbpath))
    Title = input(' Add a Video Title \n')
    Clip_Credit = input('Add a Clip Credit \n')
    des = open(f'{os.path.dirname(__file__)}/../mydescription.txt',
               'r', encoding='UTF-8').readlines()
    Data_Des = ''
    for Line in des:
        if 'Credits' in Line:
            Line = Line.rstrip()
            Line = Line.replace(Line, f"{Line}{Clip_Credit}\n")
        Data_Des += Line
    upload_obj.details(D_Tiltle=Title, D_Description=Data_Des)
    exit()


@app.command(help="Download Video from Reddit and Upload to Youtube")
def redditupload():
    typer.echo(
        "Precaution: Please Close The Chrome Application or any other tabs before using")
    rl = input(' Add Reddit Video Link:-\n').lower()
    Download(rl, destination=os.getcwd())
    info(os.getcwd()+'\Redditdownloaded.mp4')


@app.command(help="Upload a Local Video to Youtube")
def localupload():
    typer.echo(
        "Precaution: Please Close The Chrome Application or any other tabs before using")
    videopath = input('paste the absolute video path \n')
    info(videopath)


@app.command(help="Download Video from Youtube and Upload to Youtube")
def youtubeupload():
    typer.echo(
        "Precaution: Please Close The Chrome Application or any other tabs before using")
    videolink = input('Add Youtube Video Link:-\n').lower()
    a = YTdownload(str(videolink))
    videopath = a.Download()
    info(videopath)


if __name__ == "__main__":
    app()
