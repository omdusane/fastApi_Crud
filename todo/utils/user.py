from fastapi import HTTPException, status
from sqlalchemy.orm import Session
from .. import models, schemas
from ..hashing import Hash

def create(request: schemas.User, db:Session):
    """
    Create a new user.
    Parameters:
        - request: User details.
        - db: Database session.
    Returns:
        The newly created user.
    """    
    new_user = models.User(name=request.name, email=request.email, password=Hash.bcrypt(request.password))
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

def show(id:int, db: Session):
    """
    Retrieve a user by their ID.
    Parameters:
        - id: ID of the user to retrieve.
        - db: Database session.
    Returns:
        The user with the specified ID.
    """
    user = db.query(models.User).filter(models.User.id == id).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"user with this {id} is not available")

    return user