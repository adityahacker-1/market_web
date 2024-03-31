from market import db


class User(db.Model):
    id=db.Column(db.Integer,primary_key=True,nullable=False)
    username=db.Column(db.String(length=30),nullable=False,unique=True)
    email_address=db.Column(db.String(length=50),nullable=False,unique=True)
    password_hash=db.Column(db.String(length=60),nullable=False)
    budget=db.Column(db.Integer(),nullable=False,default=1000)
    items=db.relationship('Item',backref='owned_user',lazy=True)
    

class Item(db.Model):
    id=db.Column(db.Integer,primary_key=True,nullable=False)
    name=db.Column(db.String(80),nullable=False,unique=True)
    price=db.Column(db.Integer,nullable=False,unique=False)
    barcode=db.Column(db.String(80),nullable=False,unique=True)
    description=db.Column(db.String(1024),nullable=False,unique=True) 
    owner=db.Column(db.Integer(),db.ForeignKey('user.id'))
    
    def __repr__(self):
        return f'Item {self.name}'
       