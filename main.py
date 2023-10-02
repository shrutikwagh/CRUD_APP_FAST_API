from fastapi import FastAPI
import uvicorn
import hashlib

# File
import models   # Models File
import shcemas  # Schemas File
import db as db   # Database File
app=FastAPI()
# Create all tables in the database on startup
db.Base.metadata.create_all(db.engine)

# CREATE
@app.post('/create-user')
def create_user(user: shcemas.User):
    print(user)
    print(user,type(user),'*********')
    password = hashlib.sha256(user.password.encode()).hexdigest()   # Hash Password
    newuser = models.Users(name=user.name, email=user.email, password=password) # create new user instance
    db.session.add(newuser) # add user instance
    db.session.commit() # commit changes
    db.session.refresh(newuser) # Refresh the data

    return newuser  #   return newuser


@app.get('/get_users')
def get_users():
    users = db.session.query(models.Users).all()    # fetch all users
    return users    # return users

@app.get('/get_user/{id}')
def get_user(id: int):
    user = db.session.query(models.Users).filter(models.Users.id == id).first() # fetch specefic user
    return user # return user


@app.put('/update_user/{id}')
def update_user(user: shcemas.User, id: int):
    password = hashlib.sha256(user.password.encode()).hexdigest()  # Hash password
    theuser = db.session.query(models.Users).filter(models.Users.id == id).first()  # update user instance
    theuser.name = user.name  # update name
    theuser.email = user.email  # update email
    theuser.password = password  # update password

    db.session.commit()
    db.session.refresh(theuser)

    return theuser  # return theuser


@app.delete('/delete_user/{id}')
def delete_user(id: int):
    user = db.session.query(models.Users).filter(models.Users.id==id).first()   # get user by id
    db.session.delete(user) # delete instance
    db.session.commit() # commit changes

    return {'deleted'}


@app.get("/")
async def index():
   return {"data":"Welcome to my project"}


if __name__ == '__main__':
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)

