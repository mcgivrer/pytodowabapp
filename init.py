import sqlite3
conn = sqlite3.connect('todo.db') # Warning: This file is created in the current directory
conn.execute("DROP TABLE IF EXISTS author ");
conn.execute("DROP TABLE IF EXISTS todo ");
conn.execute("DROP TABLE IF EXISTS tasks ");


conn.execute("CREATE TABLE IF NOT EXISTS author (id INTEGER PRIMARY KEY, username VARCHAR(100) NOT NULL, surname VARCHAR(100), firstname VARCHAR(100), lastname VARCHAR(100), email VARCHAR(255) NOT NULL)")
conn.execute("CREATE TABLE IF NOT EXISTS todo (id INTEGER PRIMARY KEY, name VARCHAR(100) NOT NULL, author INTEGER NOT NULL, priority INTEGER DEFAULT 0,FOREIGN KEY(author) REFERENCES author(id))")
conn.execute("CREATE TABLE IF NOT EXISTS task (id INTEGER PRIMARY KEY, author INTEGER, todoId INTEGER NOT NULL, description VARCHAR(400) NOT NULL, status INTEGER NOT NULL, priority INTEGER DEFAULT 0,FOREIGN KEY(author) REFERENCES author(id),FOREIGN KEY(todoId) REFERENCES todo(id))")

conn.execute("INSERT INTO author (username, surname, firstname, lastname, email) VALUES ('212391884','Fred D.','Frédéric','Delorme','frederic.delorme@ge.com')")
conn.execute("INSERT INTO todo (name, author, priority) VALUES ('Fred''s tasks','212391884',0)")
conn.execute("INSERT INTO task (description, author, todoId , status, priority) VALUES ('Read A-byte-of-python to get a good introduction into Python (https://bottlepy.org/docs/dev/tutorial_app.html)','212391884',1,0,1)")
conn.commit()