import mysql.connector as sql
mydb = sql.connect(host = 'localhost',user ='root',passwd = "123456",
)
print(mydb)
