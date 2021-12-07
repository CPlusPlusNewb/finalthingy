from os.path import exists
import time
import colored_text_module as ctm

def clear4():
    if os.name == 'nt':
        bashcmd('cls')
    else:
        bashcmd('clear')

def writeanindex(filepath):
    file_exists = exists(filepath)
    if (file_exists == False):
        ctm.error('FILE DETECTION', 'index.html does not exist, making you a basic one now', 'blue', False)
        f = open(filepath + "/index.html", "w")
        f.write("<html><p>hola!</p></html>")
        f.close()
        #the sleep is useless, just makes them think its doing hard work lmfao
        time.sleep(4)
    else:
        clear4()
        ctm.error('FILE DETECTION', 'index.html already exsists', 'blue', False)
        time.sleep(2)
