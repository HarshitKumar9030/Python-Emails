import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import os
import time
from datetime import datetime

def sendMail(fromEmail, toEmail, subject, message):
    try:
        msg = MIMEMultipart()
        msg['From'] = fromEmail
        msg['To'] = toEmail
        msg['Subject'] = subject
        msg.attach(MIMEText(message, 'plain'))
        
        smtp_server = os.getenv('SMTP_SERVER')
        smtp_port = os.getenv('SMTP_PORT')
        smtp_email = os.getenv('SMTP_EMAIL')
        smtp_password = os.getenv('SMTP_PASSWORD')
        
        if not smtp_server or not smtp_port or not smtp_email or not smtp_password:
            print("SMTP configuration is missing. Please check environment variables.")
            return False
        
        with smtplib.SMTP(smtp_server, int(smtp_port)) as mailserver:
            mailserver.ehlo()
            mailserver.starttls()  # For security
            mailserver.login(smtp_email, smtp_password)
            mailserver.sendmail(fromEmail, toEmail, msg.as_string())
        return True
    except Exception as e:
        print(f"Failed to send email to {toEmail}. Error: {str(e)}")
        return False

def validate_email(email):
    if "@" not in email or "." not in email.split("@")[-1]:
        return False
    return True

def main():
    isSuccess = False

    input("Welcome to Email Marketing | Press Enter to start\t")
    time.sleep(0.2)
    print("It is advised to read documentation.")
    time.sleep(0.4)

    name = input("Enter your name: ")
    time.sleep(0.2)
    sEmail = input("Enter the sender's email: ")
    if not validate_email(sEmail):
        print("Invalid sender's email format. Exiting.")
        return

    eSubject = input("Enter the Subject of the Email: ")
    eMessage = input(f"Enter your Message | You can use variables like {sEmail}: ")

    time.sleep(0.3)
    print("If there are more than 1 email, they must be separated by spaces.")
    time.sleep(2)

    emailList = [item.strip() for item in input("Enter receiver's email(s): ").split()]
    emailList = [email for email in emailList if validate_email(email)]

    if not emailList:
        print("No valid emails provided. Exiting.")
        return

    for email in emailList:
        if not sEmail or not eSubject or not eMessage:
            print("Error | Missing essential email fields. Please restart the program.")
            return

        now = datetime.now()
        current_time = now.strftime("%H:%M:%S")
        if sendMail(sEmail, email, eSubject, eMessage.format(sEmail=sEmail)):
            print(f"Mail sent to {email} at {current_time}")
            isSuccess = True
        time.sleep(2)

    if isSuccess:
        current_time_loop = datetime.now().strftime("%H:%M")
        print(f"All emails sent successfully at {current_time_loop}")

if __name__ == "__main__":
    main()
