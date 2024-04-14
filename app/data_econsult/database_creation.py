import sqlite3

# Connect to SQLite database
conn = sqlite3.connect('database.db')
cursor = conn.cursor()

# Create users table
cursor.execute('''CREATE TABLE IF NOT EXISTS users (
                    id INTEGER PRIMARY KEY,
                    username TEXT NOT NULL,
                    password TEXT NOT NULL
                  )''')
name_list = ['Aaliyah Livingston',
            'Ayla Taylor',
            'Romeo Morgan',
            'Susannah Zimmerman',
            'Aaryan Reese']

password_list = ['Ay&PHJYpTb+6',
                 'N17SLT*E?qhw',
                 'ExIn%S7x*8R,',
                 'O0XqQB_JB?I3',
                 'n?ktZStD?GM2'
                ]
                         
# Insert sample data
for name, pwd in zip(name_list, password_list):
    cursor.execute("INSERT INTO users (username, password) VALUES (?, ?)", (name, pwd))


# Commit changes and close connection
conn.commit()
conn.close()