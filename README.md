# 手速脚本1.0使用指南 
现在目前还比较简陋，但能用了
## tips
+ 目前只支持发送1个附件
+ 目前只支持qq邮箱发
+ 接受邮箱不限
+ 记得更改默认的邮箱和密钥
+ 注意全角符号变成半角符号
+ 目前精确到毫秒级，我个人测试延迟大概是1.2s
+ 点击发送后脚本会一直无响应，不要动它，也不要关闭它，正确发送后它会弹出信息
## Q&A
1、 什么是邮箱密钥

	看这个：https://service.mail.qq.com/cgi-bin/help?subtype=1&id=28&no=1001256
2、 附件放在哪？

    跟这个exe文件放在同级目录里
    文件名需要加后缀 
3、时间怎么填？

    24小时制，精确到毫秒级，格式%hh:%mm:%ss.%ff，比如希望邮件在19点10分00秒发出，
	可以填19:10:00.000000
	另外如果时间小于10，需要补0，如09:01:01.123456
	如果想更精确的发邮件，时间略微提前1秒，也可以用毫秒精确控制
	
