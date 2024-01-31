import shutil
import os
import time
from pathlib import Path
class FileOrganizer :

    """
    ///////////////////////////////////////////////////////////////////////////////////
    Delete Screenshots Method: Removes all screenshots that are on the Desktop
    ///////////////////////////////////////////////////////////////////////////////////
    """
    def delete_screenshots(self):
        #delete screenshots on desktop that are more than a 2 days old
        path = "/Users/thomaszeller/Desktop"
        for i in os.listdir(path):
            if(i[0:10] == "Screenshot" and time.time() - os.path.getctime(path + "/" + i) > 172800):
               os.remove(path + "/" + i)
    """
    ///////////////////////////////////////////////////////////////////////////////////
    Clean Folder Methods: Deletes Pictures that are 2 months old and documents that are 3 months old from directory
    ///////////////////////////////////////////////////////////////////////////////////
    """
    # Clean images and PDFs and Word Documents oolder than 8 weeks from path
    def cleanFolder(self, path):
        try:
            fileList = os.listdir(path)
            for file in fileList:
                self.removeOldFile(path, file)
        except FileNotFoundError as e:
            print("File not found")
            
    # Helper for cleanFolder
    def removeOldFile(self, path, file):
        if file[-4:] == ".jpg" or file[-5:] == ".jpeg" or file[-5:] == ".HEIC" or file[-4:] == ".png":
            if (time.time() - os.path.getctime(path + "/" + file) > 482840):
                os.remove(path + "/" + file)
        elif file[-5:] == ".xlsx" or file[-5:] == ".docx" or file[-4:] == ".pdf":
            if (time.time() - os.path.getctime(path + "/" + file) > 482840.0 * 1.5):
                os.remove(path + "/" + file)