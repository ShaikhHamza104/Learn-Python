class InvalidPass(Exception):
    def __init__(self,msg):
        self.error_massage=msg


try:
    password=input("Enter a password: ")
    if not password.isalnum() or len(password)<10:
        raise InvalidPass("Password can be contain alphabet or digit and password can not less then 10 character or dont use special character ")
except InvalidPass as e:
    print(e)