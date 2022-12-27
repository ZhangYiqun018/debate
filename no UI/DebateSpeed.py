import datetime
import smtplib
import time
from email.mime.application import MIMEApplication
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import argparse

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
		# qq
		# host_server = 'smtp.qq.com'
		host_server = 'smtp.sina.com'
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
				print(f"设定时间:{self.time}\n发送时间: {start}\n延迟：{ms}")
				return [self.time, start, ms]


def testTime(sender, pwd, receiver, file_name, title, content):
	totalTime = 0
	iters = 20
	delay = 6
	for i in range(iters):
		# setTime = datetime.datetime.now().strftime('%H:%M:%S.%f')
		setTime = (datetime.datetime.now() + datetime.timedelta(seconds=2)).strftime('%H:%M:%S.%f')
		setTime, startTime, delayTime = ToEmail(setTime, sender, pwd, receiver, file_name, title, content).run()
		totalTime += delayTime
		time.sleep(delay)

	print(f"共测试{iters}次, 平均延迟：{totalTime/iters}ms")

if __name__ == '__main__':
	parser = argparse.ArgumentParser(
		description = 'argpase of auto email'
	)
	# 发送时间
	parser.add_argument(
		'--time',
		type = str,
		help = 'time: format{hh:mm:ss.xxx}'
	)
	# 发送邮箱
	parser.add_argument(
		'--to',
		type    = str,
		default = '875977494@qq.com',
		help    = 'receiver',
	)
	# 设置邮件主题
	parser.add_argument(
		'--title',
		type=str,
		default='test',
	)
	# 设置文件名
	parser.add_argument(
		'--file',
		type=str,
		default='这是测试.xlsx',
	)
	# 初始化参数
	args = parser.parse_args()
	print(args)
	setTime   = args.time
	receiver  = args.to
	file_name = args.file
	title     = args.title
	content   = args.title

	# sender = '875977494@qq.com'
	sender = 'a464849627@sina.com'
	# qq
	# pwd = 'bcycomisbtisbege'
	# sina
	pwd = '6682437211568111'
	# receiver = '875977494@qq.com'
	# file_name = '莱布尼茨不吃泡芙队+第一届泡芙杯网络辩论赛.xlsx'
	# title = '莱布尼茨不吃泡芙队+第一届泡芙杯网络辩论赛'
	# content = '莱布尼茨不吃泡芙队+第一届泡芙杯网络辩论赛'
	ToEmail(setTime, sender, pwd, receiver, file_name, title, content).run()

# python DebateSpeed.py --file 莱布尼茨不吃泡芙队+第一届泡芙杯网络辩论赛.xlsx --title  莱布尼茨不吃泡芙队+第一届泡芙杯网络辩论赛 --to 875977494@qq.com --time 10:57:59.000