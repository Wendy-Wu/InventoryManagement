'''
Created on Mar 15, 2016

@author: wuw7
'''
from IM import db
from IM.model.User import User
from IM.model.Inventory import Inventory

db.create_all()
#
inv1 = Inventory( '2000', 'Oberon cDVT system', '100-542-897-03', 'CF2ED142300019', 'FedEx hawb: 609011623649', 'Expense', 'Arrived on 6/27/2014', 'ok', 'wendy')
inv2 = Inventory( '2000.1', 'Oberon cDVT SP', '110-297-000A-03', 'CF2CT142300028', 'FedEx hawb: 609011623649', 'Expense', 'Arrived on 6/27/2016', 'ok', 'wendy')
inv3 = Inventory( '2000.2', 'Oberon cDVT SP', '110-297-000A-03', 'CF2CT142300034', 'FedEx hawb: 609011623649', 'Expense', 'Arrived on 6/27/2017', 'ok', 'wendy')

user1 = User('admin', 'admin@emc.com', 'admin')
user2 = User('wendy', 'wendy@emc.com', 'wendy')

db.session.add(inv1)
db.session.add(inv2)
db.session.add(inv3)
db.session.commit()

db.session.add(user1)
db.session.add(user2)
db.session.commit()