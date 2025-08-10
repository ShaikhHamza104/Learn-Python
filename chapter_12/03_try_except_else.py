try:
    n=int(input("Enter a number you want to print table: "))

except ValueError:
    print("Enter a valid number. Neither floating point number nor character ")

except Exception as e:
    print(e)

else:
    for i in range(1,11,1):
        print(f"{n} X {i} = {n*i}")