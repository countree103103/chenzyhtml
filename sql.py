import sqlite3
import sys

reload(sys)
sys.setdefaultencoding('utf-8')

class Sqlite():

    def __init__(self,db_adr):
        self.connection=sqlite3.connect(str(db_adr),check_same_thread=False)
        self.cur=self.connection.cursor()

    def __del__(self):
        self.connection.close()

    def insert_one(self,col,condition,data):
        self.cur.execute('insert into {} ({}) values ({})'.format(str(col),str(condition),str(data)))
        self.connection.commit()

    def insert_one(self,col,data):
        self.cur.execute('insert into {} values ({})'.format(str(col),str(data)))
        self.connection.commit()

    def find_one(self,col,pattern,data):
        result=self.cur.execute('select * from {} where {} glob "{}"'.format(str(col),str(pattern),str(data)))
        return result.fetchone()

    def find_all(self,col):
        result=self.cur.execute('select * from {}'.format(col))
        return result.fetchall()

    def close(self):
        self.connection.close()

    def update_one(self,col,key,data,rkey,rdata):
        result = self.cur.execute('update {} set {} = "{}" where {} glob "{}"'.format(col,key,data,rkey,rdata))
        self.connection.commit()

if __name__=="__main__":
    db=Sqlite("/root/chenzyhtml_test/db/db.db")
    print(db.find_all("lyb"))
