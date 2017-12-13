import sqlite3
conn = sqlite3.connect('todo.db') # Warning: This file is created in the current directory
conn.execute("CREATE TABLE task (id INTEGER PRIMARY KEY, description VARCHAR(400) NOT NULL, status INTEGER NOT NULL, priority INTEGER DEFAULT 0)")
conn.execute("CREATE TABLE todo (id INTEGER PRIMARY KEY, name VARCHAR(100) NOT NULL, author char(40) NOT NULL, priority INTEGER DEFAULT 0)")
conn.execute("INSERT INTO task (description, status) VALUES ('Read A-byte-of-python to get a good introduction into Python (https://bottlepy.org/docs/dev/tutorial_app.html)',0)")
conn.commit()