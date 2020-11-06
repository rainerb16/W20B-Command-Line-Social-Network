import dbcreds
import mariadb

def userSignup():
  conn = None
  cursor = None
  try:
    conn = mariadb.connect(user = dbcreds.user, password = dbcreds.password, port = dbcreds.port, database = dbcreds.database, host = dbcreds.host)
    cursor = conn.cursor()
    username = input("Please type in a username: ")
    password = input("Please type in a password: ")

    if len(password) < 6:
      print("Password must be 6 characters or more")
    else:
      cursor.execute("INSERT INTO hackers(alias, password) VALUES(?, ?)", [username, password,])
      conn.commit()

    if(cursor.rowcount == 1):
      print("Hacker has been created!")
    else:
      print("Something went wrong, Hacker was not created.")

  except mariadb.ProgrammingError:
    print("Sorry, a Hacker here made a programming error!")
  except mariadb.OperationalError:
    print("There was a connection error!")
  finally:
    if cursor != None:
      cursor.close()
    if conn != None:
      conn.rollback()
      conn.close()


def userLogin():
  conn = None
  cursor = None
  try:
    conn = mariadb.connect(user = dbcreds.user, password = dbcreds.password, port = dbcreds.port, database = dbcreds.database, host = dbcreds.host)
    cursor = conn.cursor()

    username = input("Please enter your username: ")
    password = input("Please enter your password: ")
    cursor.execute("SELECT * FROM hackers WHERE alias = ? AND password = ?", [username, password])
    users = cursor.fetchall()
    
    if cursor.rowcount == 1:
      for user in users:
        print("Welcome " + user[0] + " !")

      userOption = input("What would you like to do?\n1.Make new Exploit?\n2.View all of your Exploits?\n3.See Exploits by other Hackers?\n4.Logout ")

      if userOption == "1":
        content = input("Please add an exploit: ")
        cursor.execute("INSERT INTO exploits(content, id) VALUES(?, NULL)", [content,])
        conn.commit()

        if(cursor.rowcount == 1):
          print("Exploit has been created!")
        else:
          print("Something went wrong, Exploit was not created.")

      elif userOption == "2":
        cursor.execute("SELECT * FROM exploits WHERE alias = ?", [username,])
        exploits = cursor.fetchall()
        for exploit in exploits:
          print("All of your Exploits: " + exploits)

      elif userOption == "3":
        cursor.execute("SELECT * FROM exploits EXCEPT alias = ?", [username,])
        exploits = cursor.fetchall()
        for exploit in exploits:
          print("Other Hackers' Exploits: " + exploits)
    
      elif userOption == "4":
        cursor.close()
        conn.rollback()
        conn.close()
        print("You're logged out!")
      else:
        print("There was an error! Please make a selection")

    elif cursor.rowcount == 0:
      print("No Matching User!")
    else:
      print("Something went wrong...")

  except mariadb.ProgrammingError:
    print("Sorry, a Hacker here made a programming error!")
  except mariadb.OperationalError:
    print("There was a connection error!")
  finally:
    if cursor != None:
      cursor.close()
    if conn != None:
      conn.rollback()
      conn.close()
  

print("WELCOME TO HACKER NET! Please select from below: ")

userSelection = input("Press 1 to sign up\nPress 2 to login ")

if userSelection == "1":
  userSignup()
elif userSelection == "2":
  userLogin()
else:
  print("Please make a valid selection!")