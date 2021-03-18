from datetime import datetime
import pymongo
from PyQt5 import QtCore, QtWidgets

connectMongoDB = 'mongodb+srv://thanapat:thithi41@cluster0.yl4di.mongodb.net/<dbname>?retryWrites=true&w=majority'

ordermenu = []
toorder = []

def clearorder():
    ordermenu.clear()
    toorder.clear()

def order(name,type,price,amount):
    order = {'name': str(name), 'type': str(type), 'price': float(price), 'amount': int(amount)}
    ordermenu.append(order)

def getIDOrder():
    with (pymongo.MongoClient(connectMongoDB)) as conn:
        db = conn.get_database('Project_Pizza')
        where = {}
        sortz = [("_id", -1)]
        cursor = db.Order.find(where).sort(sortz).limit(1)
        res = list(cursor)
        print(res)
        if len(res) == 0:
            return 1
        else:
            for i in res:
                lastID = i['order_id']
            return lastID + 1

def getOrder():
    return ordermenu

def gettoOrder():
    datenow = datetime.now()
    id = getIDOrder()
    order = []
    for i in ordermenu:
        menu = {'name': i['name'], 'type': i['type'], 'price': i['price'], 'amount': i['amount']}
        order.append(menu)
    toorder.append(id)
    toorder.append(datetime)
    toorder.append(order)
    with (pymongo.MongoClient(connectMongoDB)) as conn:
        db = conn.get_database('Project_Pizza')
        db.Order.insert_one({'order_id': id, 'date': datenow,'items': order})

def removeOrder(row):
    del ordermenu[row]

def getOrderPrint():
    return toorder