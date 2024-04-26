from typing import List
from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from .. import schemas, models, database, oauth2
from ..utils import todo

router = APIRouter(
    prefix='/todo',
    tags=['todos']
)
get_db = database.get_db


#Get all todos
@router.get('/', status_code=200, response_model=List[schemas.ShowTodo])
def get_all(db: Session = Depends(get_db), current_user:schemas.User=Depends(oauth2.get_current_user)):
    return todo.get_all(db,current_user.email)
    

# create todo
@router.post('/', status_code=status.HTTP_201_CREATED)
def create(request: schemas.Todo, db: Session = Depends(get_db), current_user:schemas.User=Depends(oauth2.get_current_user)):
    return todo.create(request, db, current_user.email)

#get one todo
@router.get('/{id}', status_code=200, response_model=schemas.ShowTodo)
def get_one(id:int,db: Session = Depends(get_db), current_user:schemas.User=Depends(oauth2.get_current_user)):
    return todo.show(id,db)

#delete one todo
@router.delete('/{id}', status_code=status.HTTP_204_NO_CONTENT)
def delete_one(id:int, db: Session = Depends(get_db), current_user:schemas.User=Depends(oauth2.get_current_user)):
    return todo.destroy(id, db)

# Update
@router.put('/{id}',status_code=status.HTTP_202_ACCEPTED)
def update_one(id:int, request: schemas.Todo, db: Session = Depends(get_db), current_user:schemas.User=Depends(oauth2.get_current_user)):
    return todo.update(id, request, db)
