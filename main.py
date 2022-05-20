import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import os
import time
from datetime import datetime
isSuccess = False

input("Welcome to Email Marketing | Press Enter to start\t")
time.sleep(0.2)
print("It is advised to read documentation.")
time.sleep(0.4)
name = input("Enter your name : ")
time.sleep(0.2)
sEmail = input("Enter the sender's email : ")
eSubject = input("Enter the Subject of the Email : ")
eSubject = eval("f'{}'".format(eSubject))
time.sleep(0.3)
print("If there are more than 1 email , they must be seperated by\nspaces.")
time.sleep(2)
emailList = []
emailList = [item for item in input("Enter reciever's email(s) : ").split()]
eMessage = input("Enter your Message | You can use variables i.e {sEmail} : ")
eMessage = eval("f'{}'".format(eMessage))

def sendMail(fromEmail, toEmail, subject, message):
  msg = MIMEMultipart()
  msg.set_unixfrom(name)
  msg['From'] = fromEmail
  msg['To'] = toEmail
  msg['Subject'] = subject
  msg.attach(MIMEText(message))
  mailserver = smtplib.SMTP(os.environ['Smtp'], os.environ['Port'])
  mailserver.ehlo()
  mailserver.login(os.environ['email'], 
  os.environ['password']) 
  
  mailserver.sendmail(fromEmail, toEmail, 
  msg.as_string())
  mailserver.quit()
  
for email in emailList:
 if(sEmail==''):
  print("Error | Please restart the program")
  break
 elif sEmail.find("@") == -1:
  print("An email must contain a @!")
  print("Error | Please restart the program")
  break   
 elif(eSubject==''):
   print("Error | Please restart the program")
   break
 elif(eMessage==''):
   print("Error | Please restart the program")
   break
 elif email.find("@") == -1:
  print("An email must contain a @!")
  print("Error | Please restart the program")
  break
 else:
  now = datetime.now()
  current_time = now.strftime("%H:%M:%S secs ")
  fromEmail = sEmail
  subject = eSubject
  message = eMessage
  sendMail(fromEmail, email, subject, message)
  # unComment the above to use
  print(f"Mail sent to - {email} at {current_time}")
  time.sleep(2)
  isSuccess = True

if(isSuccess == True):
  now_loop = datetime.now()
  current_time_loop = now.strftime("%H:%M ")
  print(f"All emails sent successfully at {current_time_loop}")
