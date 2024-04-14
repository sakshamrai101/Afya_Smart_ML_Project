import sqlite3

# Connect to SQLite database
conn = sqlite3.connect('database_specialists.db')
cursor = conn.cursor()

# Create users table
cursor.execute('''CREATE TABLE IF NOT EXISTS users (
                    id INTEGER PRIMARY KEY,
                    username TEXT NOT NULL,
                    password TEXT NOT NULL
                  )''')
name_list = [
            'Keaton Gaines',
            'Faizan Morrison',
            'Alessia Blanchard',
            'Lily-Mae Houston',
            'Isaac Sparks']

password_list = [
                 '7m&yW3bT95%H',
                 '?18SEWtM8E;X',
                 'u!ZQJYH&.878',
                 'Z&.1N_:%S6!,',
                 '16HA&;?7PGtU'
                ]
                         
# Insert sample data
for name, pwd in zip(name_list, password_list):
    cursor.execute("INSERT INTO users (username, password) VALUES (?, ?)", (name, pwd))


# Commit changes and close connection
conn.commit()
conn.close()