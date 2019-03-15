user_name = "Munmun"
pwd = "hello"
name = input('Enter Username:\n').strip()
password = input('Enter password:\n').strip()
if name == user_name and password == pwd:
    print("Welcome, %s!" %user_name)
elif name == user_name and password != pwd:
    print("Wrong Password !")
elif name != user_name and password == pwd:
    print("Wrong user name ")
elif name != user_name and password != pwd:
    print("Wrong Details ")
