import zipfile
import sys
from threading import Thread
from colorama import Fore
from colorama import Style

#def crackzip(zfile, passwd):
#    try:
#        zfile.extractall(path='./unlocked', pwd=passwd)
#        return True
#    except:
#        pass
#    return False
def main():
    tryCount = 0
    dictionary_file = 'test.txt'
    zip_file = 'locked.zip'
    zfile = zipfile.ZipFile(zip_file, 'r')
    pfile = open(dictionary_file, 'r')

    print("***DECRYPTION START ***")
    for line in pfile.readlines():
        tryCount += 1
        passwd = line.strip('\n')
        print(f'** {Fore.RED}NOW DECRYPTING ....%d {Style.RESET_ALL} trying {Fore.GREEN} %s {Style.RESET_ALL}' %(tryCount, passwd))
#        t = Thread(target=crackzip, args = (zfile, passwd.encode('utf-8')))
#        t.start()
        try:
            zfile.extractall(path='./unlocked', pwd=passwd.encode('utf-8'))
            print("!!")
        except:
            pass
        else:
            print("**SUCCESS!! password is %s" %(passwd))
            break
    print("** FINISHED **")
main()
