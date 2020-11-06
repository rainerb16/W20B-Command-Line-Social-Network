import mariadb
import dbcreds


def userSignup(username, password):
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
                print("Welcome " + user[0] + " !")
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
def postExploit(username, content):
    conn = None
    cursor = None
    try:
        conn = mariadb.connect(user=dbcreds.user, password=dbcreds.password, port=dbcreds.port, database=dbcreds.database, host=dbcreds.host)
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM hackers WHERE alias = ?", [username, ])
        userId = cursor.fetchone()
        cursor.execute("INSERT INTO exploits(content, user_id) VALUES(?, ?)", [content, userId[0]])
        conn.commit()

        if(cursor.rowcount == 1):
            print("Exploit has been created!")
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


# GET OWN EXPLOITS
def myExploits(username):
    conn = None
    cursor = None
    try:
        conn = mariadb.connect(user=dbcreds.user, password=dbcreds.password, port=dbcreds.port, database=dbcreds.database, host=dbcreds.host)
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM hackers WHERE alias = ?", [username, ])
        user = cursor.fetchone()
        cursor.execute("SELECT * FROM exploits WHERE user_id = ?", [user[0], ])
        exploits = cursor.fetchall()
        for exploit in exploits:
            print("All of your Exploits: " + exploits)

        if(cursor.rowcount == 0):
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


# GET OTHER HACKERS' EXPLOITS
def otherHackerExploits(username):
    conn = None
    cursor = None
    try:
        conn = mariadb.connect(user=dbcreds.user, password=dbcreds.password, port=dbcreds.port, database=dbcreds.database, host=dbcreds.host)
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM hackers WHERE alias = ?", [username, ])
        users = cursor.fetchall()
        for user in users:
            cursor.execute(
                "SELECT * FROM exploits WHERE user_id = ?", [user[0], ])
            exploits = cursor.fetchall()
            for exploit in exploits:
                print("Here are what other Hackers are saying: ")

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


def userLogout():
    conn = None
    cursor = None
    conn = mariadb.connect(user=dbcreds.user, password=dbcreds.password, port=dbcreds.port, database=dbcreds.database, host=dbcreds.host)
    cursor = conn.cursor()
    cursor.close()
    conn.rollback()
    conn.close()
    print("You're logged out!")
