class Password:
    def __init__(self, username,password):
        self.username = username
        self.password = password
    def setpassword(Password,sername,password):
        password = password
        sername = sername
        if sername== Password.username and password == Password.password:
            print('login successfully ')
            file=open("translation.py",'r')
            content=file.read()
            print(content)
        else:
            print('enter again')
passw=Password('siddhesh','sid123')
passw.setpassword(str(input('enter your username: ')),str(input('enter password: ')))
