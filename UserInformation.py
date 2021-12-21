class User():
    def __init__(self, name, email, password, pwd):
        self.name = name
        self.email = email
        self.pwd = pwd
        self.password = password

u0 = User('新用户', '', '111111', '')
u1 = User('Admin', '875977494@qq.com', 'darkspiderman', 'enuhxtcuorumbbeg')
u2 = User('张媛芳', '2766366959@qq.com', '123581321zyf20011022', 'syzdmhtsfdlkdgdc')
u3 = User('韩睿', '303683509@qq.com', '123456', 'pztrvgkquisxbhgj')
u4 = User('么保鑫', '408456762@qq.com', '123456', 'wxrxjpxiwefkbgeh')
u5 = User('杨晗旖', '869804595@qq.com', '123456', 'smhqxqlgndvpbedh')
users = [u0, u1, u2, u3, u4, u5]