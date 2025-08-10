import smtplib
import  json
def read_data_from_file():
    with open("C:\\Users\\kmoha\\Desktop\\pr\\mail\\password.txt", "r") as p:
        data = json.loads(p.read())
        my_email = data.get("sender_email")
        password = data.get("password")
        receiver_email = data.get("receiver_email")
    return my_email,password,receiver_email
if __name__ == '__main__':
    EMAIL ,PASSWORD,FROM_ADDRESS= read_data_from_file()
    with smtplib.SMTP('smtp.gmail.com') as connection :
        connection.starttls()
        connection.login(user=EMAIL, password=PASSWORD)
        connection.sendmail(from_addr=EMAIL, to_addrs=FROM_ADDRESS, msg='Subject:Hello\n\nThis is the body of my email')
