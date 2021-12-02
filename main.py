import sqlite3

conn = sqlite3.connect(":memory:")

try: # MAKE THE DATABASE IF IT DOESN'T ALREADY EXIST
    conn.execute("""CREATE TABLE userSettings (Field text, Value text)""")

    name = input("\nWelcome \n\nPlease enter your name:\n\t")
    conn.execute(f"INSERT INTO userSettings VALUES ('Username', '{name}')")
    print(100*"\n")
finally:
    c = conn.cursor()
    c.execute("SELECT * FROM userSettings WHERE Field='Username'")

    user = c.fetchone()[1]
    print(f"\n\nHi, {user}\n\n")

tasks = input("What would you like to do today? \n--> ")


conn.commit()
