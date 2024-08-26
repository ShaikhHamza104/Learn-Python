import pyttsx3
engine = pyttsx3.init()
print("Welcome to robo speaker 1.1 Created by 'Hamza shaikh'")
while True:
    user_query=input("Enter what you want to speake?\n")
    engine.say(user_query)
    if user_query=='q':
        break
engine.runAndWait()