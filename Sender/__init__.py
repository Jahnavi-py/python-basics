''''from math_operations import add
def send_email(email, a, b):
    result = add(a, b)
    email_body = f"The result of adding {a} and {b} is {result}."
    print(f"Sending email to {email} with the message:\n{email_body}")
email = "jahnavi.2397@gmail.com "
a = 5
b = 7
send_email(email, a, b)'''
import smtplib
from email.mime.text import MIMEText
from math_operations import add
def send_email(email, a, b):
    result = add(a, b)
    email_body = f"The result of adding {a} and {b} is {result}."
    sender_email = "bharadwajahnavi1005@gmail.com"  # Replace with your email
    sender_password = "Brady@143"  # Replace with your password
    subject = "Calculation Result"
    message = MIMEText(email_body, "plain")
    message["From"] = sender_email
    message["To"] = email
    message["Subject"] = subject
    try:
        with smtplib.SMTP("smtp.gmail.com", 587) as server:
            server.starttls()  # Secure the connection
            server.login(sender_email, sender_password)
            server.sendmail(sender_email, email, message.as_string())
            print(f"Email sent successfully to {email}")
    except Exception as e:
        print(f"Failed to send email: {e}")
    print(f"Sending email to {email} with the message:\n{email_body}")
email = "jahnavi.2397@gmail.com "
a = 5
b = 7
send_email(email, a, b)