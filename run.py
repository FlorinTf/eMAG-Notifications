from Emag_Selenium.Emag import Emag_bot
from Emag_Selenium import Notifications

with Emag_bot() as bot:
    bot.sel_laptop()
    bot.filtre()
    bot.report_laptop()

Notifications.prices()
Notifications.send_mail()
Notifications.send_sms()
