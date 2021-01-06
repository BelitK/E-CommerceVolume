
def connect_firat(database):
    '''insert database name for variable'''
    import mysql.connector as mysql
    mydb = mysql.connect(
    host="######",
    user="####",
    database=str(database),
    password="######"
    )
    return mydb


mydbs = connect_firat("####")
curs = mydbs.cursor()
curs.execute("SELECT ECOMSA FROM ECOMSA")
results = curs.fetchall()

print(results[0])
