import os 
import shutil
import time

def main():
    deletedfolderscount=0
    deletedfilescount=0
    path='/c99project'
    days=30
    seconds=time.time()-(days*24*60*60*)
    if os.path.exists(path):
        for rootfolder,folders,files in os.walk(path):
            if seconds>=getfilesorfolderage(rootfolder):
                removefolder(rootfolder)
                deletefolderscount+=1
                break 

            else:
                for folder in folders:
                    folderpath=os.path.join(rootfolder,folder)getfilesorfoldersage
                    if seconds>=getfilesorfolderage(folderpath):
                        removefolder(folderpath)
                        deletedfolder+=1
                for file in files:
                    filepath=os.path.join(rootfolder,file)
                   if seconds>=getfilesorfolderage(rootfolder):
                        removefolder(rootfolder)
                        deletefolderscount+=1
        else:
            if seconds>=getfilesorfolderage(path):
                    removefiles(path)
                    deletefilescount+=1

    else:
        print(f'"{path}" is not found"') 
        deletefilescount+=1
    print(f'total folders deleted:{deletedfolderscount}')
    print(f'total files deleted:{deletedfilesscount}')

def removefolders(path):
    if not shutil.rmtree(path):
        print(f'{path}is removed successfully')
    else:
        print(f'{path}path cannot be deleted')

def removefiles(path):
    if not os.remove(path):
        print(f'{path}is removed successfully')
    else:
        print(f'{path}path cannot be deleted')

def getfilesorfolderage(path):
    ctime=os.stat(path).st_ctime
    return ctime

if __name__=='__main__':
    main()








