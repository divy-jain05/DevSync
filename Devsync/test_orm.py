from app.database import engine
from app.models import User
from sqlalchemy.orm import Session

with Session(engine) as session:
    users = session.query(User).all()
    print("Connection successful!")
    for user in users:
        print(f"ID: {user.id} | Name: {user.name} | Role: {user.role}")
        
