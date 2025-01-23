valid=False             
while not valid:
    try:
        n=int(input("enter a no:"))
        while n%2==0:
            print("bye")
            valid=True   
    exception ValueError:
        print("invalid")