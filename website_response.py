import requests, smtplib
from threading import Thread
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase

## Mention your websites in this list.
ourwebsite = [
		'Websites'
	]

body = """
"""
a = []

class Feedex:
	username = "Email_User"
	password = "Email_User_Password"
	def __init__(self, host="smtp.gmail.com", port=587):
		try:
			self.connection = smtplib.SMTP(host, port)
		except Exception as e:
			print(e)
			exit()
		else:
			self.connection.starttls()
	def authentication(self):
		try:
			self.connection.login(Feedex.username, Feedex.password)
		except Exception as e:
			print(e)
			exit()
	def feedexmail(self, to_user, msgbody):
		try:
			self.connection.sendmail(Feedex.username, to_user, msgbody)
		except Exception as e:
			print(e)
			exit()

def main():
	msg = MIMEMultipart()

	to = 'TO Email Address'
	cc = 'One_Email_Address,Two_Email_Address'
	rcpt = cc.split(",") + [to]

	msg['From'] = 'Email_User'
	msg['To'] = to
	msg['cc'] = cc
	msg['Subject'] = 'Subject'

	msg.attach(MIMEText(body,'plain'))
	text = msg.as_string()

	mail_class_obj = Feedex()
	mail_class_obj.authentication()
	mail_class_obj.feedexmail(rcpt, text)

def check_website(onewebsite):
	try:
		reach_to_website = requests.get(onewebsite)
	except Exception as e:
		b = "{} some different error {}\n".format(onewebsite, e)
		a.append(b)
	else:
		if reach_to_website.status_code != 200:
			b = "{} response code is {}\n".format(onewebsite, reach_to_website.status_code)
			a.append(b)

if __name__ == '__main__':
	for i in ourwebsite:
		t = Thread(target=check_website, args=(i,))
		t.start()
		ourwebsite.remove(i)
		t.join()
	body = "".join(a)
	main()