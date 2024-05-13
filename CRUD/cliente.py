import CRUD as c
#read
def read():
    dades=[]
    mycursor = c.mydb.cursor(dictionary=True)
    mycursor.execute("SELECT * FROM clients WHERE id= result['id']")
    dades = mycursor.fetchall()
    mycursor.close()
    return dades


def list():
    dades=[]
    mycursor = c.mydb.cursor(dictionary=True)
    mycursor.execute("SELECT * FROM client")
    dades = mycursor.fetchall()
    mycursor.close()
    return dades


def create(nom, cognom1,cognom2, telefon):
    id=()
    mycursor = c.mydb.cursor()
    sql = """INSERT INTO client (nom, cognom1, cognom2,telefon) 
        VALUES (%s, %s, %s, %s)"""
    mycursor.execute(sql, [nom, cognom1,cognom2, telefon])
    c.mydb.commit()
    id = mycursor.lastrowid 
    print(f"hddhhdhsahdjaidbiasb{id}")
    mycursor.close()
    return id