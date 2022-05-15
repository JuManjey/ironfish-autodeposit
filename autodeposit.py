from operator import eq
import subprocess

print("Start of work")
bashCommand = ["yarn", "--cwd", "/root/ironfish/ironfish-cli/", "start", "accounts:balance"]
process = subprocess.Popen(bashCommand, stdout=subprocess.PIPE)
output, error = process.communicate()
massive2 = output.split()

massive_of_spend_balance = ((str)(massive2[36])).strip()
if ((str)(massive_of_spend_balance[2])) == "0":             
    print("Выход! Баланса недостаточно")
else:                    
    print("Выполнение операции депозита")
    bashCommand = ["yarn", "--cwd", "/root/ironfish/ironfish-cli/", "start", "deposit", "--confirm"]
    process = subprocess.Popen(bashCommand, stdout=subprocess.PIPE)
    output, error = process.communicate()
    print(output)
    import datetime
    e = datetime.datetime.now()
    print ("Current date and time = %s" % e)
    print ("Today's date:  = %s/%s/%s" % (e.day, e.month, e.year))
    print ("The time is now: = %s:%s:%s" % (e.hour, e.minute, e.second))
