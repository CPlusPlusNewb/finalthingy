import os
bashcmd = os.system

def check_for_installs_coltext():
    installed_colorama = False
    installed_termcolor = False
    try:
        import colorama
    except ImportError as e:
        bashcmd('sudo apt install python3-colorama')
        bashcmd('clear')
        installed_colorama = True

    try:
        import termcolor
    except ImportError as e:
        bashcmd('sudo apt install python3-termcolor')
        bashcmd('clear')
        installed_termcolor = True

    if (installed_colorama == True):
        error('SUCCESS', 'Installed python3-colorama', 'green', False)
    if (installed_termcolor == True):
        error('SUCCESS', 'Installed python3-termcolor', 'green', False)

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
