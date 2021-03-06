from Emag_Selenium.Emag import timex,laptop_list
from twilio.rest import Client
from email.message import EmailMessage
import os
import smtplib
import imghdr

EMAIL_PASSWORD = os.environ.get('password')
text_sms = ''
def prices():
    for i in laptop_list:
        price = i['price'][0:-7]
        price1 = price.replace('.', '')
        if int(price1) < 5400:
            text_sms = (f'Emag {i["title"][0:36]} - {price} lei')
        else:
            pass

def send_mail():
    msg = EmailMessage()
    msg["Subject"] = "Laptopuri Emag"
    msg["From"] = "code@gmail.com"
    msg["To"] = 'email.xxxx@yahoo.com'
    msg.set_content(f"{laptop_list[0]['title']} - {laptop_list[0]['price']} \n\n"
                    f"{laptop_list[1]['title']} - {laptop_list[1]['price']}\n\n"
                    f"{laptop_list[2]['title']} - {laptop_list[2]['price']}")
    with open('laptop'+timex+'.png', "rb") as f:
        file_data = f.read()
        file_type = imghdr.what(f.name)
        file_name = f.name
    msg.add_attachment(file_data, maintype="image", subtype=file_type, filename=file_name)
    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        smtp.login("code@gmail.com", EMAIL_PASSWORD)
        smtp.send_message(msg)

def send_sms():
    if text_sms == '':
        pass
    else:
        account_sid = 'AKJdg48738f7hjxhb'
        auth_token = 'fdgdf75fa6fdf76gdf8hf7gh96'
        client = Client(account_sid, auth_token)
        message = client.messages.create(
            messaging_service_sid='MG8bc5vkdh65hfghfg4h#',
            body=text_sms,
            to='+4073xxxxxx'
        )
