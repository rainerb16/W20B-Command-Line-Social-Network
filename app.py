import dbcreds
import mariadb
import functions

print("WELCOME TO HACKER NET! Please select from below: ")

while True:
    userSelection = input("Press 1 to Login\nPress 2 to Sign Up ")
    print()

    if userSelection == "1":
        username = input("Please enter your username: ")
        password = input("Please enter your password: ")
        print()
        user = functions.userLogin(username, password)
        if user:
            while True:
                menuSelection = input("1. Post new Exploit\n2. See your own Exploits\n3. See other Hackers' Exploits\n4. EXIT ")
                print()
                if menuSelection == "1":
                    content = input("Please enter Exploit: ")
                    functions.postExploit(content, user)
                elif menuSelection == "2":
                    functions.myExploits(user)
                elif menuSelection == "3":
                    functions.otherHackerExploits(user)
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

