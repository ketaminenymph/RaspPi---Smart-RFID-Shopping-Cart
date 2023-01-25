import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522
import urllib.request
import yagmail
import os
from InvoiceGenerator.api import Invoice, Item, Client, Provider, Creator
from InvoiceGenerator.pdf import SimpleInvoice

user = *enter your email id*
app_password = *generated password*
to = *customer's email id*
subject = "Your Receipt. Thank you, Visit again"
subject1 = 'System is up'
subject2 = "System Down"
content = ['.']


def connect(host='http://google.com'):
    try:
        urllib.request.urlopen(host)
        return True
    except:
        return False

print("Connected" if connect() else "no internet")

def status():
    with yagmail.SMTP(user, app_password) as yag:
        yag.send(to, subject1, content)
        print('Sent email successfully')

def status1():
    with yagmail.SMTP(user, app_password) as yag:
        yag.send(to, subject2, content)
        print('Sent email successfully')
    

def read():
    reader = SimpleMFRC522()
    try:
        print('Place item on reader')
        id = reader.read()
        id, text = reader.read()
        print(id)
        if id == 717502388296:
            print('success')
        else:
            pass

    finally:
        GPIO.cleanup()

def main():
    if connect():
        status()
    else:
        status1()
    read()

if __name__ == "__main__":
    main()
