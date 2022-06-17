import sys
import time
import datetime
import smtplib
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication 

class ToEmail():
	def __init__(self, time, sender, pwd, receiver, file_name, title, content):
		self.sender = sender
		self.pwd = pwd
		self.receiver = receiver
		self.filename = file_name
		s = datetime.datetime.now().strftime('%Y-%m-%d ')
		self.time = datetime.datetime.strptime(s + time, '%Y-%m-%d %H:%M:%S.%f')
		self.title = title
		self.content = content
	def send_email(self):
		host_server = 'smtp.qq.com'
		# pwd = 'bcycomisbtisbege'
		# pwd = 'enuhxtcuorumbbeg'

		textApart = MIMEText(self.content)

		# root = '/root/spider/debate/'
		# imageFile = '这是测试.png'
		# imageApart = MIMEImage(open(root + imageFile, 'rb').read(), imageFile.split('.')[-1])
		# imageApart.add_header('Content-Disposition', 'attachment', filename=imageFile)

		excelFile = self.filename
		excelApart = MIMEApplication(open(excelFile, 'rb').read())
		excelApart.add_header('Content-Disposition', 'attachment', filename=excelFile)

		m = MIMEMultipart()
		m["Subject"] = self.title
		m["From"]    = self.sender
		m["To"]      = self.receiver

		m.attach(textApart)
		# m.attach(wordApart)
		m.attach(excelApart)
		# m.attach(pdfApart)
		# m.attach(imageApart)

		server = smtplib.SMTP_SSL(host_server)
		server.set_debuglevel(0)
		server.ehlo(host_server)
		server.login(self.sender, self.pwd)
		server.sendmail(self.sender, self.receiver, m.as_string())
		server.quit()

	def run(self):
		while True:
			start = datetime.datetime.now()
			# print(self.time, start)
			ms = (self.time - start).total_seconds() * 10**6
			if abs(ms) <= 1000:
				self.send_email()
				start = datetime.datetime.now()
				ms = (start - self.time).total_seconds() * 10**3
				# print(start, self.time, ms)
				return [start, ms]

if __name__ == '__main__':
	time = "17:10:00.000"
	sender = '875977494@qq.com'
	pwd = 'cihxsigbxvfxbeej'
	receiver = '875977494@qq.com'
	file_name = '这是测试.xlsx'
	title = '这是测试'
	content = '这是测试'
	t = ToEmail(time, sender, pwd, receiver, file_name, title, content)
	t.run()