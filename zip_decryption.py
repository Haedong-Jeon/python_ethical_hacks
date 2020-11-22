import zipfile
from threading import Thread

def crackzip(zfile, passwd):
    try:
        zfile.extractall(path='./unlocked', pwd=passwd)
        return True
    except:
        pass
    return False

def main():
    dictionary_file = 'dictionary.txt'
    zip_file = 'locked.zip'
    zfile = zipfile.ZipFile(zip_file, 'r')
    pfile = open(dictionary_file, 'r')

    print("*** DECRYPTION START  ***")
    for line in pfile.readlines():
        passwd = line.strip('\n')
        t = Thread(target=crackzip, args = (zfile, passwd))
        t.start()
    print("** FINISHED **")

main()
