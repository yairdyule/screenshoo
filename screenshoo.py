#!/usr/bin/python

import os
import schedule
import time

# in macos, screenshots goto desktop (ugly, smh)
# so, this script sends them all to a dump directory

path = "/Users/jaredjewell/Desktop"
dirname = "!#&$ screenshots"

def moveScreenshots():

    os.chdir(path) # goto desktop

    # make our dump dir if !exists already 
    if not os.path.isdir(dirname):
        os.mkdir(dirname)

    # move every screenshot to ...../dirname
    with os.scandir() as it:
        for entry in it:
            if entry.is_file() and entry.name.startswith("Screen Shot"):
                os.rename(entry.name, "/".join((path, dirname, entry.name)))

schedule.every().day.at("01:00").do(moveScreenshots)

while True:
    schedule.run_pending()
    time.sleep(60*60) # wait an hour
