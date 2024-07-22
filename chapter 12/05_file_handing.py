try:
    file=input("Enter file name you want to open ")
    f=open(file)
except FileNotFoundError:
    print(f"{file} not found Error")
else:
    data=f.read()
    print(data)
finally:
    f.close()