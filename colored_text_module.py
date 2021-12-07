import os
import getfile as gf
bashcmd = os.system

def downloadpipfile2(file):
    if os.name == 'nt':
        bashcmd('pip install ' + file)
    else:
        bashcmd('sudo apt install ' + file)

def clear2():
    if os.name == 'nt':
        bashcmd('cls')
    else:
        bashcmd('clear')

def check_for_installs_coltext():
    installed_colorama = False
    installed_termcolor = False
    try:
        import colorama
    except ImportError as e:
        downloadpipfile2('colorama')
        clear2()
        installed_colorama = True

    try:
        import termcolor
    except ImportError as e:
        downloadpipfile2('termcolor')
        clear2()
        installed_termcolor = True

    if (installed_colorama == True):
        error('SUCCESS', 'Installed python colorama', 'green', False)
    if (installed_termcolor == True):
        error('SUCCESS', 'Installed python termcolor', 'green', False)

def error(problem, text2, color, blink):#this is mucho epico
    # \/ THIS IS PROBABLY SUPER INEFFICIENT, BUT IDC REALLY
    check_for_installs_coltext()
    from colorama import Fore, Back, Style 
    from termcolor import colored, cprint 
    text1 = ''
    if (blink == True):
        text1 = colored('[' + problem + ']', color, attrs=['blink', 'bold']) 
    else:
        text1 = colored('[' + problem + ']', color, attrs=['bold']) 
    print(text1, end="") 
    #print(Fore.RED + '[' + problem + ']', end="") 
    print(Style.RESET_ALL, end=" ") 
    print(text2)
