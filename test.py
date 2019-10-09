import mysql.connector

mydb = mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    database="testdb"
)

mycursor = mydb.cursor()

# mycursor.execute("SHOW TABLES")

# for table in mycursor:
#     print(table)
# mycursor.execute("CREATE TABLE students (name VARCHAR(255), age INTEGER(10))")
sqlFormula = "INSERT INTO students (name, age) VALUES (%s, %s)"
students = [("Chandler", 24),
            ("Ross", 24),
            ("Pheobe", 23),
            ("Joey", 24),
            ("Mike", 24)]

mycursor.executemany(sqlFormula, students)

mydb.commit()

