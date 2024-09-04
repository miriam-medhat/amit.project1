from LIBRARY import library

lib = library()

while True:
    action = input("Enter the number of your choice: \n1.show games\n2.lend a game\n3.return a game\n4.donate a game\n5.exit\n")
    if action == "1":
        lib.games()
    elif action == "2":
        lib.lend()
    elif action == "3":
        lib.returnb()
    elif action == "4":
        lib.donate()
    elif action == "5":
        break
    else:
        print("invalid choice")
