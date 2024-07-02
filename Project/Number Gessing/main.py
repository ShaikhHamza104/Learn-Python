def game():
        gesses=1
        print("............. Welcome to Number gessing game .............")
        while True:
                user=int(input("Gesses the number : "))
                if user<com:
                        print("You enter more value ...")
                        gesses+=1
                elif user>com:
                        print("You enter less value ...")
                        gesses+=1
                elif com==user:
                        gesses+=1
                        print("You win ")
                        print(f"You can gesse the number in  {gesses}")
                        # print("Thank you for using this game\nhave a good day")
                        break
if __name__=="__main__":
        import random
        com=random.randint(1,100)
        game()
        # print(com)