from flask_sqlalchemy import SQLAlchemy # Use the docs to see how we input into this
from flask_migrate import Migrate

db = SQLAlchemy() #create an instance of a databacse connection
migrate = Migrate(db) # associate migration functions to it

#this ORM has the migration and the model together
class User(db.Model):
    # this is the migration part
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True) #column is a class of SQLAlchemy, which we have caled db
    username = db.Column(db.String(80), unique=True, nullable=False) #80 is the maxlength of string acceptable. these arevalidations
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, server_default=db.func.now(), server_onupdate=db.func.now())

    # this is regular old python classes
    # right here is where we whitelist what can be set when creating a user 
    #any column omitted cannot be set by the user/app manually

    # essentially the allowed parameters. 
    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.password = password

    def __repr__(self):
        return '<User %r>' % self.username #another type of string interpolation
