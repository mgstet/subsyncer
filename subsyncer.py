#!/usr/bin/python

import os
import subprocess
import shutil
import glob

vids = sorted(glob.glob("*.mkv"))
subs = sorted(glob.glob("*.srt"))

os.mkdir("temp")

for vid, sub in zip(vids, subs):
    command = ["alass", "-O", "0", "-g", "-p", "5", f"{vid}", f"{sub}", f"temp/{sub}"]
    subprocess.run(command)

for sub in subs:
    shutil.move(f"temp/{sub}", sub)

os.rmdir("temp")

