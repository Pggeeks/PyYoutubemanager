import os

import typer
from rich import print

from download import YTdownload
from reddownloder import Download
from uploader import upload

app = typer.Typer(add_completion=False,
    help= typer.secho('''
    • Welcome To Youtube Manager New To The App Check XP_conf.py File First.
    • Upload Videos to Youtube With Description,Title,Credits,Thumbnail Of your own Choice and much more.
    • Download Video from Reddit,Youtube,Local Storage.
    • --addtext | Display the Giving Text on Top Left Of the Video for 8 seconds. currently supported only for \n      redditupload / use [command] --addtext
    ''', fg=typer.colors.BRIGHT_YELLOW)
    )

def info(videoadd):
    upload_obj = upload(videoadd)
    upload_obj.send()
    print('[bold red]Alert![/bold red] [yellow]Want to add a thumbnail? press Y/N:-[/yellow]')
    thumbnail_or_not = input('').lower()
    if thumbnail_or_not == "y":
        print('[bold red]Alert![/bold red] [yellow]Paste the absolute path of Thumbnail:-[/yellow]')
        thumbpath = input('')
        upload_obj.Thumbnail(str(thumbpath))
    print('[bold red]Alert![/bold red] [yellow] Input a Video Title:-[/yellow]')
    Title = input('')
    print('[bold red]Alert![/bold red] [yellow]Input Clip Credits! Leave this if no credits defined in mydescription.txt:-[/yellow]')
    Clip_Credit = input('')
    des = open(f'{os.path.dirname(__file__)}./mydescription.txt',
               'r', encoding='UTF-8').readlines()
    if Clip_Credit == '' or None:
        upload_obj.details(D_Tiltle=Title, D_Description=des)
        exit()
    ## if credits finds credit word in description and add input there.
    Data_Des = ''
    for Line in des:
        if 'Credits' in Line:
            Line = Line.rstrip()
            Line = Line.replace(Line, f"{Line}{Clip_Credit}\n")
        Data_Des += Line
    upload_obj.details(D_Tiltle=Title, D_Description=Data_Des)
    exit()

@app.command(help="Download Video from Reddit and Upload to Youtube")
def redditupload(addtext: bool = typer.Option(False,prompt="want to display Text On Video? mainly used for giving credits?",help="Display the Giving Text on Top Left Of the Video for 8 seconds. currently supported only for reddituploader / use [command] --addtext"),):
    print("[bold red]Alert![/bold red] [yellow]Precaution: Please Close The Chrome Application or any other tabs before using[/yellow]")
    print('[bold red]Alert![/bold red] [yellow]Input A Reddit Video Link:-[/yellow]')
    rl = input('').lower()
    if addtext:
        print('[bold red]Alert![/bold red] [yellow]Enter Text You Want To display on video:-[/yellow]')
        text = input().lower()
        Download(rl, destination=os.getcwd(),addtext=True,text=text)
    else:
        Download(rl, destination=os.getcwd())
    info(os.getcwd()+'\Redditdownloaded.mp4')



@app.command(help="Upload a Local Video to Youtube")
def localupload():
    print("[bold red]Alert![/bold red] [yellow]Precaution: Please Close The Chrome Application or any other tabs before using[/yellow]")
    print('[bold red]Alert![/bold red] [yellow]Paste The Absolute Path Of Video[/yellow]')
    videopath = input('')
    info(videopath)


@app.command(help="Download Video from Youtube and Upload to Youtube")
def youtubeupload():
    print("[bold red]Alert![/bold red] [yellow]Precaution: Please Close The Chrome Application or any other tabs before using[/yellow]")
    print('[bold red]Alert![/bold red] [yellow]Input Youtube Video Link:-[/yellow]')
    videolink = input('').lower()
    a = YTdownload(str(videolink))
    videopath = a.Download()
    info(videopath)


if __name__ == "__main__":
    app()
