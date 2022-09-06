import subprocess
import datetime
import os
import struct
from time import sleep

print("Start of work")
bashCommand = ["yarn", "--cwd", "/root/ironfish/ironfish-cli/", "start", "accounts:balance"]
process = subprocess.Popen(bashCommand, stdout=subprocess.PIPE)
output, error = process.communicate()
massive = output.decode("utf-8")
massive2 = massive.split()
count = float(massive2[40])
name_of_client = str(massive2[26])
if count > 1:
    bashCommand = ["yarn", "--cwd", "/root/ironfish/ironfish-cli/", "start", "deposit", "--confirm"]
    process = subprocess.Popen(bashCommand, stdout=subprocess.PIPE)
    os.system("curl https://api.telegram.org/bot5291389******/sendMessage?chat_id=178*** -d text=Депозит\ " + str(name_of_client) + "\ У\ Вас\ на\ балансе\ " + str(count))
exit()
