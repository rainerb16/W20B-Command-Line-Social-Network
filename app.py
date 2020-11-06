import dbcreds
import mariadb
import functions

print("WELCOME TO HACKER NET! Please select from below: ")

while True:
    userSelection = input("Press 1 to Login\nPress 2 to Sign Up ")
    print()

    if userSelection == "1":
        username = input("Please type in a username: ")
        password = input("Please type in a password: ")
        print()
        if functions.userLogin(username, password):
            while True:
                menuSelection = input("1. Post new Exploit\n2. See your own Exploits\n3. See other Hackers' Exploits\n4. EXIT ")
                print()
                if menuSelection == "1":
                    content = input("Please add an exploit: ")
                    functions.postExploit(username, content)
                elif menuSelection == "2":
                    functions.myExploits(username)
                elif menuSelection == "3":
                    functions.otherHackerExploits(username)
                elif menuSelection == "4":
                    functions.userLogout()
                else:
                    print("Please make a valid selection...")
                break

    elif userSelection == "2":
        username = input("Please enter a username: ")
        password = input("Please enter a password: ")
        if len(password) < 6:
            print("Password must be 6 characters or more")
        else:
            functions.userSignup(username,password)

    else:
        print("There was an error")
    break

