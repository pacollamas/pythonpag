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

def create(nom, cognom1,cognom2, telefon):
    mycursor = c.mydb.cursor()
    sql = """INSERT INTO client (nom, cognom1, cognom2,telefon) 
        VALUES (%s, %s, %s, %s)"""
    mycursor.execute(sql, [nom, cognom1,cognom2, telefon])
    c.mydb.commit()
    count = mycursor.rowcount
    mycursor.close()
    return count