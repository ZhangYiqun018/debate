import sys
import time
import datetime
import smtplib
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication 
import tkinter
import tkinter.messagebox

class ToEmail():
	def __init__(self, time, sender, pwd, receiver, file_name, title, content):
		self.sender = sender
		self.pwd = pwd
		self.receiver = receiver
		self.filename = file_name
		self.time = datetime.datetime.strptime(time, '%H:%M:%S.%f')
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

		try:
			server = smtplib.SMTP_SSL(host_server)
			server.set_debuglevel(0)
			server.ehlo(host_server)
			server.login(self.sender, self.pwd)
			server.sendmail(self.sender, self.receiver, m.as_string())
			server.quit()

		except smtplib.SMTPException as e:
			print('error:', e)

	def run(self):
		while True:
			start = datetime.datetime.now()
			ms = (start - self.time).seconds
			if abs(ms) <= 200:
				self.send_email()
				break
			time.sleep(0.0000001)

def quit():
	sys.exit()

def process():
	time = E_time.get()
	sender = E_from.get()
	pwd = E_pwd.get()
	receiver = E_to.get()
	filename = E_filename.get()
	title = E_title.get()
	content = E_content.get()
	e = ToEmail(time, sender, pwd, receiver, filename, title, content)
	e.run()
	NowTime = datetime.datetime.now().strftime('%H:%M:%S.%f')
	tkinter.messagebox.showinfo( "发送状态", "发送时间:" + NowTime + "\n发送者:" + sender + "\n接受者:" + receiver + "\n发送成功！")

if __name__ == '__main__':
	r = tkinter.Tk()
	r.title('自动发邮件1.0')
	r.geometry("800x600")

	L_time = tkinter.Label(r, text="\n发送时间(%h:%m:%s.%f)")
	L_time.pack()
	E_time = tkinter.Entry(r, bd=4)
	E_time.pack()

	L_from = tkinter.Label(r, text="发送的邮箱")
	L_from.pack()
	E_from = tkinter.Entry(r, bd=4)
	E_from.insert(tkinter.END, '875977494@qq.com')
	E_from.pack()

	L_pwd = tkinter.Label(r, text="邮箱密钥")
	L_pwd.pack()
	E_pwd = tkinter.Entry(r, bd=4)
	E_pwd.insert(tkinter.END, 'enuhxtcuorumbbeg')
	E_pwd.pack()

	L_to = tkinter.Label(r, text="接受的邮箱")
	L_to.pack()
	E_to = tkinter.Entry(r, bd=4)
	E_to.insert(tkinter.END, '875977494@qq.com')
	E_to.pack()

	L_filename = tkinter.Label(r, text="要发送的文件名")
	L_filename.pack()
	E_filename = tkinter.Entry(r, bd=4)
	E_filename.insert(tkinter.END, '校队考勤.xlsx')
	E_filename.pack()

	L_title = tkinter.Label(r, text="邮件标题")
	L_title.pack()
	E_title = tkinter.Entry(r, bd=4)
	E_title.insert(tkinter.END, 'test')
	E_title.pack()

	L_content = tkinter.Label(r, text="邮件内容")
	L_content.pack()
	E_content = tkinter.Entry(r, bd=4)
	E_content.insert(tkinter.END, 'test')
	E_content.pack()

	B1 = tkinter.Button(r, text="点我发邮件", command=process)
	B1.pack()
	B2 = tkinter.Button(r, text="取消", command=quit)
	B2.pack()

	L_text = tkinter.Label(r, text="\n网辩拼手速脚本\n使用方法见readme.md\n目前只支持qq邮箱发送，接收方邮箱不限\nhttps://github.com/ZhangYiqun018/debate\nby 张逸群", fg = 'grey')
	L_text.pack(side = tkinter.RIGHT)

	r.mainloop()