import os
import shutil
source = input("enter source folder name:")
destination = input("enter the destination name:")
listOfFiles = os.listdir(source)
for file in listOfFiles:
    shutil.move((source+file),destination)
    