"""
   This is a model to copy the content from old file to new file.
   read 50 characters from oldfile and write them to the newfile.
   When read util the end of old file, fileContent=="" establish, the function ends.
"""

def copy_file(oldfile,newfile):
    oldFile=open(oldfile,"r")
    newFile=open(newfile,"a")
    while True:
        fileContent=oldFile.read(50)
        if fileContent=="":
            break
        newFile.write(fileContent)
    oldFile.close()
    newFile.close()
    print("Copy Finished!")