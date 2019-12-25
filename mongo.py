# -*- coding: utf-8 -*
import pymongo
import sys

reload(sys)
sys.setdefaultencoding('utf-8')

class Mongo():
    def __init__(self,host,db_name,port=27017):
        self.client=pymongo.MongoClient(host=str(host),port=int(port))
        self.db=self.client[str(db_name)]
    def __del__(self):
        self.client.close()
    def insert_one(self,col,data):
        self.col=self.db[str(col)]
        self.col.insert_one(data)
    def find_one(self,col,data):
        self.col=self.db[str(col)]
        return self.col.find_one(data)
    def find_all(self,col,data):
        self.col=self.db[str(col)]
        return self.col.find(data)
    def close(self):
        self.client.close()

if __name__=='__main__':
    db=Mongo('localhost',db_name='sk')
    print(db.find_one(col='users',data={'name': 'czy103'}))
