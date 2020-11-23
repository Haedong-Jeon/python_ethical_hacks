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
    tryCount = 0
    dictionary_file = 'dictionary.txt'
    zip_file = 'locked.zip'
    zfile = zipfile.ZipFile(zip_file, 'r')
    pfile = open(dictionary_file, 'r')

    print("***DECRYPTION START ***")
    for line in pfile.readlines():
        tryCount += 1
        passwd = line.strip('\n')
        t = Thread(target=crackzip, args = (zfile, passwd))
        t.start()
        print('** NOW DECRYPTING... %d try' %(tryCount))
    print("** FINISHED **")

main()
