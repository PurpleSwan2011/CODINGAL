try:
    number=int(input("enter a no:"))
    print("the no entered is,number")
except ValueError as ex:
    print("exception:",ex)