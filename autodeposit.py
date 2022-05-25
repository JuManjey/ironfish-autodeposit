import subprocess
import datetime
import os
import struct
from time import sleep

print("Start of work")
e = datetime.datetime.now()
bashCommand = ["yarn", "--cwd", "/root/ironfish/ironfish-cli/", "start", "accounts:balance"]
process = subprocess.Popen(bashCommand, stdout=subprocess.PIPE)
output, error = process.communicate()
massive = output.decode("utf-8")
massive2 = massive.split()
count = float(massive2[36])
name_of_client = str(massive2[22])
if count < 1:
    os.system("curl https://api.telegram.org/bot5291389******/sendMessage?chat_id=178*** -d text=Выход\ " + "Баланса\ недостаточно\ " + str(name_of_client) + "\ У\ Вас\ на\ балансе\ " + str(count))
    exit()
else:
    os.system("curl https://api.telegram.org/bot5291389******/sendMessage?chat_id=178*** -d text=Депозит\ " + str(name_of_client) + "\ У\ Вас\ на\ балансе\ " + str(count))
    bashCommand = ["yarn", "--cwd", "/root/ironfish/ironfish-cli/", "start", "deposit", "--confirm"]
    process = subprocess.Popen(bashCommand, stdout=subprocess.PIPE)
    output, error = process.communicate()
