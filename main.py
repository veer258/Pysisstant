import sqlite3
import os.path

from Commands.Weather import weather

conn = sqlite3.connect("User_Database.db")

#Get all user info

try: # MAKE THE DATABASE IF IT DOESN'T ALREADY EXIST
    conn.execute("""CREATE TABLE userSettings (Field text, Value text)""")

    print("\n\n\nMaking your profile...\n\n\n")

    name = input("\nWelcome \n\nWhat's your name: \n--> ")
    conn.execute(f"INSERT INTO userSettings VALUES ('Username', '{name}')")

    location = input("\nEnter your location: \n--> ")
    conn.execute(f"INSERT INTO userSettings VALUES ('Location', '{location}')")

    conn.commit()

    print("\n\n---\n---\n\n")

except: pass

c = conn.cursor()
c.execute("SELECT * FROM userSettings WHERE Field='Username'")
user = c.fetchone()[1]

c.execute("SELECT * FROM userSettings WHERE Field='Location'")
location = c.fetchone()[1]

print(f"\n\nHi, {user}\n\n")

# FUNCTIONS

def task_weather():
    weatherValues = weather(location)
    return f"\nIn {location}, you will experience {weatherValues[1]} and the temperature is {round(weatherValues[0],1)}°C. \nI hope you have a lovely day!"

# MAIN LOOP
while True:
    task = input("\nWhat would you like to do today? \n--> ")

    if task == "weather":
        print(task_weather())






conn.commit()
