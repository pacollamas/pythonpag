#!/usr/bin/env python3

import mysql.connector

def connectar():
    global mydb
    print("Obrint connexió a la BD...")
    mydb = mysql.connector.connect(
        host="shared.daw.cat",
        user="1ad09",
        password="1ASIXdaw*09",
        port="3306",
        database="1ad09_my"
    )
    
def desconnectar():
    mydb.close()