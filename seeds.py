from app import app
from models import db, User

print('Seeding database ... 🌱')
# Add your seed data here
user1 = User('lar', 'lar@gmail.com', '1111')
db.session.add_all([user1])
db.session.commit()

print('Done! 🌳')