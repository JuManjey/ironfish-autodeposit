import subprocess
import datetime
import os
import struct
from time import sleep

print("Start of work")
bashCommand = ["yarn", "--cwd", "/root/ironfish/ironfish-cli/",
               "start", "accounts:balance"]
process = subprocess.Popen(bashCommand, stdout=subprocess.PIPE)
output, error = process.communicate()
massive = output.decode("utf-8")
massive2 = massive.split()
count = float(massive2[36])
name_of_client = str(massive2[22])
status = os.system('systemctl is-active --quiet service-name')
if count > 1 and status != 0:
    bashCommand = ["/etc/init.d/cron", "start"]
    sleep(5)
    bashCommand = ["yarn", "--cwd", "/root/ironfish/ironfish-cli/",
                   "start", "deposit", "--confirm"]
    os.system("curl https://api.telegram.org/bot5291389******/sendMessage?chat_id=178*** -d text=Депозит\ " + str(name_of_client) + "\ У\ Вас\ на\ балансе\ " + str(count))
    process = subprocess.Popen(bashCommand, stdout=subprocess.PIPE)
else:
    bashCommand = ["/etc/init.d/cron", "stop"]
exit()
