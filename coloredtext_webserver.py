# almost all code from preston, minus the webserver stuff from mr.coleman / icebowl,
#  and some modifications to that code from noah mcgee. Thanks to them for help
import http.server
import socketserver
import os 
import sys
import webbrowser
import writeaindex as wai
bashcmd = os.system

def getfilefromweb(file):
    if os.name == 'nt':
        bashcmd('curl.exe -O ' + file)
    else:
        bashcmd('wget ' + file)

def downloadfile(file):
    if os.name == 'nt':
        bashcmd('winget install ' + file)
    else:
        bashcmd('sudo apt install ' + file)

def downloadpipfile(file):
    if os.name == 'nt':
        bashcmd('pip install ' + file)
    else:
        bashcmd('sudo apt install ' + file)

def clear():
    if os.name == 'nt':
        bashcmd('cls')
    else:
        bashcmd('clear')

def bigline_seperator():
    import colored_text_module as ctm
    ctm.check_for_installs_coltext()
    from colorama import Fore, Back, Style 
    from termcolor import colored, cprint 
    color = 'blue'
    bigline="---------------------------------------"
    text1 = colored(bigline, color, attrs=['bold']) 
    print(text1)
    print(Style.RESET_ALL, end="") 

def main2():
    import colored_text_module as ctm
    try:
        try:
            PORT = 8080
            PORT = int(PORT)
        except ValueError as e:
            ctm.error('ERROR', 'ValueError: Please enter a number, not text', 'red', True)
            main()
        path = '.'
        bigline_seperator()
        ctm.error('LIST', 'These are the folders: ', 'green', False)
        files = os.listdir(path)
        #this finds all folders, or anything that doesn't have a period
        for name in files:
            if '.' in name: 
                print ('', end="")
            else:
                print(name)
        bigline_seperator()
        webroot = input("What folder to use as web root?: ")
        try:
            web_dir = os.path.join(os.path.dirname(__file__), webroot)
            os.chdir(web_dir)#web root
            Handler = http.server.SimpleHTTPRequestHandler
            httpd = socketserver.TCPServer(("", PORT), Handler)
            wai.writeanindex(web_dir)
            clear()
            ctm.error('SUCCESS', 'setup was successful', 'green', False)
            ctm.error('NOTICE!', 'IN ORDER TO CLOSE DO CTRL+C THEN REFRESH THE PAGE', 'red', False)
            print("serving at port", PORT)
            print("Webroot is "+webroot+'/')
            webbrowser.open('http://localhost:8080')
            try:
                httpd.serve_forever()
            except KeyboardInterrupt:
                pass
            finally:
                httpd.server_close()
        except FileNotFoundError as e:
            ctm.error('ERROR', "FileNotFoundError: that folder does't exsist", 'red', True)
            exit()
    except OSError as e:
        ctm.error('ERROR', "OSError: Program will now exit", 'red', True)
        exit()

def main():
    import colored_text_module as ctm
    ctm.check_for_installs_coltext()
    main2()

#error('Success', 'Installed python3-colorama', 'green', False)
#error('Success', 'Installed python3-termcolor', 'green', False)

if (__name__ == "__main__"):
    installed_colored_text_module = False
    installed_writeanidex = False
    try:
        import colored_text_module
    except ImportError as e:
        getfilefromweb('https://raw.githubusercontent.com/CPlusPlusNewb/python/master/colored_text_module.py')
        clear()
        installed_colored_text_module = True
#---------------------------------------------------------------------------------
    try:
        import writeaindex
    except ImportError as e:
        getfilefromweb('https://raw.githubusercontent.com/CPlusPlusNewb/python/master/writeaindex.py')
        clear()
        installed_writeanidex = True
#---------------------------------------------------------------------------------
    import colored_text_module as ctm
    if (installed_colored_text_module == True):
        ctm.error('SUCCESS', 'Installed colored_text_module.py', 'green', False)
    main()