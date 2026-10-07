

color = input("Enter traffic color: ")

match color:
    case "Green":
        print("You can go")
    case "Yellow":
        print("Wait")
    case "Red":
        print("Stop")
    case _:
        print("Wrong color")