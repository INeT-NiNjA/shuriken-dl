#(Download from youtube)#
def youtubedl():
    import os, progressbar
    from pytube import YouTube
    from pytube.request import URLError
    from pytube.exceptions import RegexMatchError
    from colorama import Fore
    import glob

    def progress(streams, chunk: bytes, bytes_remaining: int):
        contentsize = stream.filesize
        size = contentsize - bytes_remaining
        print( Fore.GREEN + '\r' + '[Download progress]:[%s%s]%.2f%%;' % (
    '█' * int(size*20/contentsize), ' '*(20-int(size*20/contentsize)), float(size/contentsize*100)), end='') 

    while True:
        try:
            os.system('clear')
            print(Fore.WHITE + ' •INeT-NiNjA/shuriken-dl/youtube-dl•')
            print()
            link = input(Fore.CYAN + " [ENTER THE LINK OF THE YOUTUBE VIDEO] \n => ")
            yt = YouTube(link,on_progress_callback=progress)
            print()
            print(Fore.YELLOW + ' ' + yt.title)
            break
        except URLError:
            print(Fore.RED + ' ** You are not connected to the internet!! **')
            quit()
        except RegexMatchError:
            print(Fore.RED + ' ** The link is not valid **')
        except KeyboardInterrupt:
            print(Fore.RED + ' ** Quitting the program **')
            quit()
        except:
            print(Fore.RED + ' ** Error..Please try again!! **')

    while True:
        print('')
        print(Fore.CYAN + ' [1] DOWNLOAD VIDEO')
        print(Fore.CYAN + ' [2] DOWNLOAD AS AUDIO')
        print(Fore.CYAN + ' [3] DOWNLOAD/VIEW THUMBNAIL')
        print(Fore.CYAN + ' [4] RETURN TO MAIN MENU')
        print('')
        try:
            choice = int(input(Fore.CYAN + ' [WHAT DO YOU WANT TO DO?]\n => '))
        except ValueError:
            choice = 5

        if choice < 1 or choice > 4:
            print(Fore.RED + " ** Please select a valid option!! **")
            continue
        if choice == 1:
            try:
                os.makedirs('youtube-dl/videos',exist_ok=True)
                print('')
                stream = yt.streams.get_by_itag(22)
                stream.download('youtube-dl/videos')
                break
            except:
                print(Fore.RED + " ** An error occured!! **")
            
        if choice == 2:
            try:
                os.makedirs('youtube-dl/music',exist_ok=True)
                print('')
                stream = yt.streams.get_by_itag(140)
                stream.download('youtube-dl/music')
                for filename in glob.iglob(os.path.join('youtube-dl/music', '*.mp4')):
                    os.rename(filename, filename[:-4] + '.mp3')
                break
            except:
                print(Fore.RED + " ** An error occured!! **")
        if choice == 3:
            try:
                print('')
                print(Fore.CYAN + ' [OPEN THIS LINK IN BROWSER TO ACCESS THUMBNAIL]')
                print('')
                print(Fore.YELLOW + yt.thumbnail_url)
                break
            except:
                print( Fore.RED + ' ** An error occured!! **')
        if choice ==4:
            youtubedl()
        if KeyboardInterrupt:
            print(Fore.RED + ' ** Quitting the program **')
            break






#(Download from facebook)
def facebookdl():
    pass










#(Main program)#
youtubedl()
