import CRUD as c
#read
def read():
    mycursor = c.mydb.cursor()
    mycursor.execute("SELECT * FROM clients WHERE id= ")
    myresult = mycursor.fetchall()
    mycursor.close()
    return myresult


def list():
    mycursor = c.mydb.cursor()
    mycursor.execute("SELECT * FROM client")
    myresult = mycursor.fetchall()
    mycursor.close()
    return myresult

# def create():
#     mycursor = c.mydb.cursor()
#     sql = """INSERT INTO dades_web (id, nom, cognom1, cognom2) 
#         VALUES (%s, %s, %s, %s)"""
#     mycursor.execute(sql, [url, categoria, data])
#     c.mydb.commit()
#     count = mycursor.rowcount
#     mycursor.close()
#     return count