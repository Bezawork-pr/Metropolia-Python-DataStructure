"""Write a program that sums all of the numbers taken as input,
while ignoring any input that is not a valid number."""
sum = 0
while True:
    myinput = input()
    check = myinput.isnumeric()
    if check == True:
        if int(myinput) == 0:
            print("The grand total is {}".format(sum))
            exit()
        sum += float(myinput)
        print("The total is now {}".format(sum))
    else:
        print("That wasn’t a number.")
        
print("The grand total is {}")
