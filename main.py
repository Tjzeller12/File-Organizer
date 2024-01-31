import shutil
import os
import time
from file_organizer import *
from pathlib import Path

def run():
    # make clean folder and delete screenshots constantly run
    file_org = FileOrganizer()
    while True:
        file_org.cleanFolder("/Users/thomaszeller/Downloads")
        file_org.delete_screenshots()
        time.sleep(10) # run every 10 seconds

run()
