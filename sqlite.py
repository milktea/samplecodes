#Milktea
#From http://stoneriverelearning.com/
#Basic Database (SQLite) with Python

#module
import sqlite3

#connecting to database
conn = sqlite3.connect('tutorial.db')
c = conn.cursor()

#creating a table named example
def create_table():
    c.execute("CREATE TABLE example(Language VARCHAR, Version FLOAT, Skill TEXT)")

#inserting static data
def enter_data():
    c.execute("INSERT INTO example VALUES('Python', '2.7', 'Beginner')")
    c.execute("INSERT INTO example VALUES('Python', '3.3', 'Intermediate')")
    c.execute("INSERT INTO example VALUES('Pyython', '3.4', 'Expert')")
    conn.commit()

#inserting dynamic data
def enter_dynamic_data():
    language = raw_input('Language: ')
    version = raw_input('Version: ')
    skill = raw_input('Skill: ')
    
    c.execute("INSERT INTO example(Language, Version, Skill) VALUES(?,?,?)",(language, version, skill))
    conn.commit()

#accessing data
def read_from_database():
    #sql = "SELECT * FROM example WHERE Skill == 'Expert' LIMIT 2"
    sql = "SELECT * FROM example"
    for row in c.execute(sql):
	print(row)

#updating data
def update_data():
    #sql = "UPDATE example SET Skill = 'beginner' WHERE Skill = 'Beginner'"
    sql = "UPDATE example SET Skill = 'intermediate' WHERE Skill = 'Intermediate'"
    c.execute(sql)
    conn.commit()
    
#deleting data
def delete_data():
   sql = "DELETE FROM example WHERE Skill = 'Intermediate'"
   c.execute(sql)
   conn.commit()

#create_table()
#enter_data()
#enter_dynamic_data()
#read_from_database()
#update_data()
#delete_data()
read_from_database()
conn.close()
