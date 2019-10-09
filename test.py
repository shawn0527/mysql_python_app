import mysql.connector

mydb = mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    database="testdb"
)

mycursor = mydb.cursor()
# mycursor.execute("SHOW TABLES")

# Tutorial 2:

# for table in mycursor:
#     print(table)
# mycursor.execute("CREATE TABLE students (name VARCHAR(255), age INTEGER(10))")
# sqlFormula = "INSERT INTO students (name, age) VALUES (%s, %s)"
# student1 = ("Rachel", 22)
# mycursor.execute(sqlSormula, student1)
# mydb.commit()

#Tutorial 3:
# students = [("Chandler", 24),
#             ("Ross", 24),
#             ("Pheobe", 23),
#             ("Joey", 24),
#             ("Mike", 24)]
# mycursor.executemany(sqlFormula, students)
# mydb.commit()

#Tutorial 4:
# mycursor.execute("SELECT age FROM students")
# myresult = mycursor.fetchone()

# for row in myresult:
#     print(row)

#Tutorial 5:
# sql1 = "SELECT * FROM students WHERE age = 22"
# sql2 = "SELECT age FROM students WHERE name = 'ROSS'"
# sql3 = "SELECT * FROM students WHERE name LIKE 'R%'"
# sql4 = "SELECT * FROM students WHERE name LIKE '%a%'"
# sql5 = "SELECT * FROM students WHERE name = %s"

# mycursor.execute(sql5, ("Ross",))

# myresults = mycursor.fetchall()

# for result in myresults:
#     print(result)

#Tutorial 6:
# sql1 = "UPDATE students SET age = 25 WHERE name = 'Ross'"
# sql2 = "SELECT * FROM students LIMIT 5"
# sql3 = "SELECT * FROM students LIMIT 3 OFFSET 2"

# mycursor.execute(sql3)

# myresults = mycursor.fetchall()

# for result in myresults:
#     print(result)

# mydb.commit()


