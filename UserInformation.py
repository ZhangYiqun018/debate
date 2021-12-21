class User():
    def __init__(self, name, email, password, pwd):
        self.name = name
        self.email = email
        self.pwd = pwd
        self.password = password

u0 = User('新用户', '', '', '')
u1 = User('张逸群', '875977494@qq.com', 'darkspiderman', 'enuhxtcuorumbbeg')
u2 = User('张媛芳', '2766366959@qq.com', '123456', 'icnhvarhzhkqdfid')
u3 = User('韩睿', '303683509@qq.com', '123456', 'pztrvgkquisxbhgj')
u4 = User('么保鑫', '2766366959@qq.com', '123456', 'icnhvarhzhkqdfid')
u5 = User('杨晗旖', '2766366959@qq.com', '123456', 'icnhvarhzhkqdfid')
users = [u0, u1, u2, u3, u4, u5]