import smtplib, ssl


host = "smtp.gmail.com"
port = 465

username = "jon@example.gmail.com"
password = ""

receiver = "jon@example.gmail.com"
context = ssl.create_default_context()

message = """
Hello there,
I am here"""

with smtplib.SMTP_SSL(host, port, context= context) as server:
    server.login(username, password)
    server.sendmail(username, receiver, message)