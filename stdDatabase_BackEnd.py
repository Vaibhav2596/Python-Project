import pymysql as p

def getConnect():
    serverName = 'localhost'
    username = 'root'
    passw = ''
    dbname = 'StudentDatabase'
    return p.connect(serverName,username,passw,dbname)

def addStdRec(StdID,Firstname,Surname,DoB,Age,Gender,Address,Mobile):
    db = getConnect()
    cur = db.cursor()
    sql = 'insert into student(StdID,Firstname,Surname,DoB,Age,Gender,Address,Mobile) values(%s,%s,%s,%s,%s,%s,%s,%s)'
    t = StdID,Firstname,Surname,DoB,Age,Gender,Address,Mobile
    cur.execute(sql,t)
    db.commit()
    db.close()

def viewData():
    db = getConnect()
    cur = db.cursor()
    sql = 'select * from student'
    cur.execute(sql)
    row = cur.fetchall()
    db.close()
    return row

def deleteRec(id):
    db = getConnect()
    cur = db.cursor()
    sql = 'delete from student where id=%s'
    cur.execute(sql,id)
    db.commit()
    db.close()

def searchData(StdID="",Firstname="",Surname="",DoB="",Age="",Gender="",Address="",Mobile=""):
    db = getConnect()
    cur = db.cursor()
    sql = 'select * from student where StdID=%s OR Firstname=%s OR Surname=%s OR DoB=%s OR Age=%s OR Gender=%s OR Address=%s OR Mobile=%s'
    t = StdID,Firstname,Surname,DoB,Age,Gender,Address,Mobile
    cur.execute(sql,t)
    rows = cur.fetchall()
    db.commit()
    db.close()
    return rows

def updateUser(id,StdID="",Firstname="",Surname="",DoB="",Age="",Gender="",Address="",Mobile=""):
    db = getConnect()
    cur = db.cursor()
    sql = 'update student set StdID=%s,Firstname=%s,Surname=%s,DoB=%s,Age=%s,Gender=%s,Address=%s,Mobile=%s where id=%s'
    t = StdID,Firstname,Surname,DoB,Age,Gender,Address,Mobile,id
    cur.execute(sql,t)
    db.commit()
    db.close()  

