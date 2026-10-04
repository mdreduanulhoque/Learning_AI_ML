color = input("Enter Traffic Light Color: ")

if (color == 'green' or color == 'Green'):
    print("You can go ... ...")
elif (color == 'Red' or color == 'red'):
    print("You can't go ... ...")
elif (color == 'yellow' or color == 'Yellow'):
    print("GEt ready, you are about to go ... ...")
else:
    print("Wrong color in input")