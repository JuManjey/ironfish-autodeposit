# ironfish-autodeposit
Create autodeposit for IronFish Node

`git clone https://github.com/JuManjey/ironfish-autodeposit.git && cd ironfish-autodeposit && chmod +x autodeposit.py  `
`touch /root/logfile.log  `
Cron:  
`nano /etc/crontab  `
Добавить:  
`*/3 * * * * root python3 /root/ironfish-autodeposit/autodeposit.py | tee -a /root/logfile.log  `
Cron:  
`systemctl enable cron && systemctl status cron && systemctl start cron  `
Смотреть:  
`tail -F /root/logfile.log  `
