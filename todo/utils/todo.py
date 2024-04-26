from fastapi import HTTPException, status
from sqlalchemy.orm import Session
from .. import models, schemas

def get_all(db: Session, current_user:str):
    """
    Retrieve all to-do items for the current user.
    Parameters:
        - db: Database session object.
        - current_user: Email address of the current user.
    Returns:
        List of to-do items belonging to the current user.
    """
    
    user = db.query(models.User).filter(models.User.email==current_user).first()
    todos = db.query(models.Todo).filter(models.Todo.user_id==user.id).all()
    return todos

def create(request: schemas.Todo, db: Session, current_user:str):
    """
    Create a new to-do item for the current user.
    Parameters:
        - request: To-do item details.
        - db: Database session.
        - current_user: Current user's email.
    Returns:
        A message and the newly created to-do item.
    """
    user = db.query(models.User).filter(models.User.email==current_user).first()
    new_todo = models.Todo(title=request.title, status=request.status, user_id=user.id)
    db.add(new_todo)
    db.commit()
    db.refresh(new_todo)

    return {"message": "todo created Successfully", "new_todo": new_todo}

def destroy(id:int, db:Session):
    """
    Delete a to-do item by its ID.
    Parameters:
        - id: ID of the to-do item to delete.
        - db: Database session.
    Returns:
        A message indicating the operation completion.
    """
    todo = db.query(models.Todo).filter(models.Todo.id==id)
    if not todo.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Todo with this {id} is not found")
    todo.delete(synchronize_session=False)
    db.commit()
    return {"message": "todo deleted Successfully"}

def update(id:int, request:schemas.Todo, db: Session ):
    """
    Update a to-do item by its ID.
    Parameters:
        - id: ID of the to-do item to update.
        - request: Updated to-do item details.
        - db: Database session.
    Returns:
        A message indicating the successful update.
    """
    todo = db.query(models.Todo).filter(models.Todo.id==id)
    if not todo.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Todo with id: {id} is not found")
    
    todo.update(request.model_dump())
    db.commit()
    return {"message": f"Updated todo with id {id}"}

def show(id:int, db: Session):
    """
    Retrieve a to-do item by its ID.
    Parameters:
        - id: ID of the to-do item to retrieve.
        - db: Database session.
    Returns:
        The to-do item with the specified ID.
    """
    todo = db.query(models.Todo).filter(models.Todo.id == id).first()
    if not todo:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Todo with this {id} is not available")

    return todo