#!/usr/bin/python

import os
import subprocess
import shutil
import glob

vids = glob.glob("*.mkv")
subs = glob.glob("*.srt")

os.mkdir("temp")

for vid, sub in zip(vids, subs):
    command = f"alass -O 0 -g -p 5 {vid} {sub} temp/{sub}".split(" ")
    subprocess.run(command)

for sub in subs:
    shutil.move(f"temp/{sub}", sub)

os.rmdir("temp")
