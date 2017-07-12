
from iglo import IGlo
from time import sleep

if __name__ == '__main__':
    iglo = IGlo('192.168.1.107')
    while True:
        iglo.send_command('ON')
        sleep(4)
        iglo.send_command('OFF') 
        sleep(4)

