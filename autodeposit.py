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
massive2 = output.split();
count = float(massive2[39])
name_of_client = str(massive2[25].decode("utf-8"))
if count < 1:
    os.system("curl https://api.telegram.org/bot5291389954:AAE-PIYhNxt_yRBwioZPjP2T6DS2IQDpf6E/sendMessage?chat_id=1740882388 -d text=Выход\ !" + "Баланса\ недостаточно\ " + str(name_of_client) + "\ У\ Вас\ на\ балансе\ " + str(count))
    sleep(300)
    exit()
else:
    os.system("curl https://api.telegram.org/bot5291389954:AAE-PIYhNxt_yRBwioZPjP2T6DS2IQDpf6E/sendMessage?chat_id=1740882388 -d text=Депозит\ !" + str(name_of_client) + "\ У\ Вас\ на\ балансе\ " + str(count))
    bashCommand = ["yarn", "--cwd", "/root/ironfish/ironfish-cli/", "start", "deposit", "--confirm"]
    process = subprocess.Popen(bashCommand, stdout=subprocess.PIPE)
    output, error = process.communicate()
