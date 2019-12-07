from dbConnection import *

conn = db_connection("chatRoom.db")
cursor = conn.cursor()

# cursor.execute("CREATE TABLE IF NOT EXISTS users(pid integer PRIMARY KEY AUTOINCREMENT , name VARCHAR(255), age integer CHECK(age > 15), gender BOOLEAN , country VARCHAR(255))")

users_list = [('ashkan', 16, True, 'Iran'), ('Benyamin', 22, True, 'Iran'), ('Ghasem', 17,
                                                                             True, 'Iran'), ('Sakineh', 19, False, 'Iran')]


#
users_list1 = [('Gholi', 19, True), ('Sara', 19, False)]
# cursor.executemany(
#     "INSERT INTO users(name, age, gender)  VALUES(?, ?, ?)", users_list1)
query = "INSERT INTO users(name, age, gender)  VALUES(?, ?, ?)"
dbQuery = dbQueryBylist(cursor, query, users_list1)

if dbQuery:
    conn.commit()

#cursor.execute("SELECT * FROM users")

#user_db_list = cursor.fetchall()

dbQuery = dbQueryByParam(cursor, "SELECT * FROM users")

if dbQuery:
    user_db_list = cursor.fetchall()

conn.close()

for user in user_db_list:
    print(user)
