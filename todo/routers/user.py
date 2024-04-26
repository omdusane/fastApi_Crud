from fastapi import APIRouter
from .. import database, schemas
from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends

from ..utils import user

router = APIRouter(
    prefix='/user',
    tags=['users']
)
get_db = database.get_db

#create user
@router.post('/', response_model=schemas.ShowUser)
def create_user(request: schemas.User, db: Session = Depends(get_db)):
    return user.create(request,db)


#get one user
@router.get('/{id}', status_code=200, response_model=schemas.ShowUser)
def get_one_user(id,db: Session = Depends(get_db)):
    return user.show(id, db)