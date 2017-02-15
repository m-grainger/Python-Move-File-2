
import time, os, shutil


def filecopy(src, dst):
    now = time.time() #Used the time module because datetime.now() won't work with the if statement below.
    docs = os.listdir(src) 
    for i in docs:
        file_name = src + '\\' + i #Grabs entire file name.  Double slash is used to add file name to file folder path.
        new_or_edited = os.stat(file_name).st_mtime #Creates variable that grabs creation/edit times
        one_day = (now - 86400)  #86400 is one day counted in seconds.
        if new_or_edited > one_day:  
            shutil.copy(file_name, dst) 
            print(file_name)


def main():
    folder_src = 'C:\\Users\\Student\\Desktop\\file-folder'
    folder_dest = 'C:\\Users\\Student\\Desktop\\new-and-edited-recently'
    filecopy(folder_src, folder_dest)

main()
