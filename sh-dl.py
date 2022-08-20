from pytube import YouTube
import progressbar as progress
import os
from pytube.exceptions import RegexMatchError
from pytube.request import URLError
import colorama
from colorama import Fore,Back

def progress(streams, chunk: bytes, bytes_remaining: int):
    contentsize = stream.filesize
    size = contentsize - bytes_remaining
    print( Fore.GREEN + '\r' + '[Download progress]:[%s%s]%.2f%%;' % (
    '█' * int(size*20/contentsize), ' '*(20-int(size*20/contentsize)), float(size/contentsize*100)), end='')

os.system('clear')
print(Fore.WHITE + " •INeT-NiNjA/shuriken-dl•")
print('')
print(Fore.BLUE + " [YOUTUBE VIDEO DOWNLOADER]\n   ")
link = input(Fore.CYAN + " [ENTER VIDEO'S LINK]\n => ")
print('')


try:
    yt = YouTube(link,on_progress_callback=progress)
    print( Fore.YELLOW + ' ' + yt.title)
except URLError:
    print(Fore.RED + ' ** Make sure you are connected to the internet **')
except RegexMatchError:
    print(Fore.RED + ' ** Make sure that the link is valid **')
except:
    print( Fore.RED + '** An error occured...Please try again **')
else:
    print('')
    print(Fore.CYAN + ' [1] DOWNLOAD VIDEO')
    print(Fore.CYAN + ' [2] DOWNLOAD AS AUDIO')
    print(Fore.CYAN + ' [3] DOWNLOAD/VIEW THUMBNAIL')
    print('')
    Choice = input(Fore.CYAN + ' [WHAT DO YOU WANT TO DO?]\n => ')
    choice = int(Choice)
    if choice == 1:
        try:
            print('')
            stream = yt.streams.get_by_itag(22)
            stream.download()
        except:
         print(Fore.RED + "An error occured!!")
    if choice == 2:
        try:
            print('')
            stream = yt.streams.get_by_itag(140)
            stream.download()
        except:
            print(Fore.RED + '  ** An error occured!! **')
    if choice == 3:
        try:
            print('')
            print(Fore.CYAN + ' [OPEN THIS LINK IN BROWSER TO ACCESS THUMBNAIL]')
            print('')
            print(Fore.YELLOW + yt.thumbnail_url)
        except:
            print( Fore.RED + ' ** An error occured!! **')
    if choice > 3 or choice < 1 or type(choice) == str:
        print( Fore.RED + " ** Please select a valid option **")
    
