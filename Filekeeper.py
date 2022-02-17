import os
import shutil
import time



def main():
    DeletedFolderCount=0
    DeletedFileCount=0

    path=""
    days=30
    seconds=time.time()-(days*24*60*60)

    if(os.path.exists(path)):
        for rootFolder,folders,files in os.walk(path):
                if(seconds>GetFolderAndFileAge(rootFolder)):
                        removeFolder(rootFolder)
                        DeletedFolderCount+=1
                        break
                else:
                        for folder in folders:
                                folderPath=os.path.join(rootFolder,folder)
                                if(seconds>=GetFolderAndFileAge(folderPath)):
                                        removeFolder(folderPath)
                                        DeletedFolderCount+=1
                        for file in files:
                                filePath=os.path.join(rootFolder,file)
                                if(seconds>=GetFolderAndFileAge(filePath)):
                                        removeFile(filePath)
                                        DeletedFileCount+=1
    else:
             print('file not found ')
    
                

            


def removeFolder(path):
    if not shutil.rmtree(path):
            print("Path removed Successfully")
    else:
            print("Path not found")


def removeFile(path):
        if not os.remove(path):
                print("Path removed Successfully")
        else:
                print('Path not found')

def GetFolderAndFileAge(path):
        ctime=os.stat(path).st_ctime
        return ctime

main()


        