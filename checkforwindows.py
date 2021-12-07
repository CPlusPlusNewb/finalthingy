import os
def main():
    if os.name == 'nt':
        print('hello')
    else:
        print('error')
main()