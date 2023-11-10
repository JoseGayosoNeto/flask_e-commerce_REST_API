from API import db
from passlib.hash import pbkdf2_sha256

class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True,nullable=False)
    name = db.Column(db.String(200), nullable=False)
    email = db.Column(db.String(200), nullable=False, unique=True)
    password = db.Column(db.String(255), nullable=False)
    address = db.Column(db.String(100), nullable=False)
    is_admin = db.Column(db.Boolean, nullable=False)


    def encrypt_password(self):
        self.password = pbkdf2_sha256.hash(self.password)
    
    def verify_password(self,password):
        return pbkdf2_sha256.verify(password,self.password)

    def __repr__(self,name,email,address,is_admin):
        return f"User('{self.name}', '{self.email}', '{self.address}' is_admin:'{self.is_admin}')"

