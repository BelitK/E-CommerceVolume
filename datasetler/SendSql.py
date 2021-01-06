
import mysql.connector
import pandas as pd

def connect_Firat(database):
  '''insert database name for variable'''
  import mysql.connector as mysql
  mydb = mysql.connect(
    host="#######",
    user="#######",
    database=str(database),
    password="######"
  )
  return mydb

mydbs = connect_Firat("#####")
def commit_data(dataname):
  '''specialized for my database insert '''
  data = pd.read_excel(str(dataname), header=0)
  dates = data["observation_date"]
  curs = mydbs.cursor()
  for number in range(len(dates)):
    #change column names
    date = str(data["observation_date"][number])
    ecomsa = str(data["ECOMSA"][number])
    #change sql query for columns
    sql = f"INSERT INTO ECOMSA (dateT, ECOMSA) VALUES (%s, %s)"
    val = (date,ecomsa)
    print(val)
    curs.execute(sql, val)
commit_data("TurkeyData3.xls")
mydbs.commit()

