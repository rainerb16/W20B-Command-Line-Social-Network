import mariadb
import dbcreds

# USER SIGNUP
def userSignup():
    conn = None
    cursor = None
    try:
        conn = mariadb.connect(user=dbcreds.user, password=dbcreds.password, port=dbcreds.port, database=dbcreds.database, host=dbcreds.host)
        cursor = conn.cursor()

        if len(password) < 6:
            print("Password must be 6 characters or more")
        else:
            cursor.execute("INSERT INTO hackers(alias, password) VALUES(?, ?)", [username, password, ])
            conn.commit()

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


#  USER LOGIN
def userLogin(username, password):
    conn = None
    cursor = None
    try:
        conn = mariadb.connect(user=dbcreds.user, password=dbcreds.password, port=dbcreds.port, database=dbcreds.database, host=dbcreds.host)
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM hackers WHERE alias = ? AND password = ?", [username, password, ])
        users = cursor.fetchall()
        
        if cursor.rowcount == 1:
            for user in users:
                print("Logged In!")
                print()
            return users[0]
        else:
            print("No Matching User Found!")

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


# POST EXPLOIT
def postExploit(content, user):
    conn = None
    cursor = None
    try:
        conn = mariadb.connect(user=dbcreds.user, password=dbcreds.password, port=dbcreds.port, database=dbcreds.database, host=dbcreds.host)
        cursor = conn.cursor()
        cursor.execute("INSERT INTO exploits(content, user_id) VALUES(?, ?)", [content, user[2]])
        conn.commit()

        if(cursor.rowcount == 1):
            print("Exploit has been created!")
            print()
        else:
            print("Something went wrong, Exploit was not created.")

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


# UPDATE POST
def updateExploit(updatedContent, id):
    conn = None
    cursor = None
    try:
        conn = mariadb.connect(user=dbcreds.user, password=dbcreds.password, port=dbcreds.port, database=dbcreds.database, host=dbcreds.host)
        cursor = conn.cursor()
        cursor.execute("UPDATE exploits SET content = ? WHERE id = ?", [updatedContent, id])
        conn.commit()

        if(cursor.rowcount == 1):
            print("Exploit has been updated!")
            print()
        else:
            print("Something went wrong, Exploit was not updated.")

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

# GET OWN EXPLOITS
def myExploits(user):
    conn = None
    cursor = None
    try:
        conn = mariadb.connect(user=dbcreds.user, password=dbcreds.password, port=dbcreds.port, database=dbcreds.database, host=dbcreds.host)
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM exploits e INNER JOIN hackers h ON e.user_id = h.id WHERE user_id = ?", [user[2], ])
        exploits = cursor.fetchall()
        for exploit in exploits:
            print("Alias: " + str(exploit[3]))
            print("Exploit Id: " + str(exploit[1]))
            print("Exploit: " + str(exploit[0]))
            print()

        if(cursor.rowcount == 0):
            print("Something went wrong.")

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


# GET OTHER HACKERS' EXPLOITS
def otherHackerExploits(user):
    conn = None
    cursor = None
    try:
        conn = mariadb.connect(user=dbcreds.user, password=dbcreds.password, port=dbcreds.port, database=dbcreds.database, host=dbcreds.host)
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM exploits e INNER JOIN hackers h ON e.user_id = h.id WHERE user_id != ?", [user[2], ])
        exploits = cursor.fetchall()
        for exploit in exploits:
            print("Alias: " + str(exploit[3]))
            print("Exploit: " + str(exploit[0]))
            print()

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


# USER LOGOUT
def userLogout(user):
    conn = None
    cursor = None
    conn = mariadb.connect(user=dbcreds.user, password=dbcreds.password, port=dbcreds.port, database=dbcreds.database, host=dbcreds.host)
    cursor = conn.cursor()
    cursor.close()
    conn.rollback()
    conn.close()
    print("You're logged out!")

