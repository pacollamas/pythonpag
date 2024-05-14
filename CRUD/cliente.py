import CRUD as c
#read
def read(id):
    dades = []
    mycursor = c.mydb.cursor(dictionary=True)
    mycursor.execute("SELECT * FROM client WHERE id = %s", (id,))
    dades = mycursor.fetchall()
    mycursor.close()
    return dades



# def read(id=None):
#     dades = []
#     mycursor = c.mydb.cursor(dictionary=True)
#     if id is not None:
#         mycursor.execute("SELECT * FROM clients WHERE id = %s", (id,))
#     else:
#         mycursor.execute("SELECT * FROM clients")
#     dades = mycursor.fetchall()
#     mycursor.close()
#     return dades



def list():
    dades=[]
    mycursor = c.mydb.cursor(dictionary=True)
    mycursor.execute("SELECT * FROM client")
    dades = mycursor.fetchall()
    mycursor.close()
    return dades

def update(id, nom, cognom1, cognom2, telefon):
    mycursor = c.mydb.cursor()
    sql = """UPDATE client SET nom=%s, cognom1=%s, cognom2=%s, telefon=%s WHERE id=%s"""
    mycursor.execute(sql, (nom, cognom1, cognom2, telefon, id))
    c.mydb.commit()
    id = mycursor.lastrowid 
    print(f"Updated record with id: {id}")
    mycursor.close()
    return id


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