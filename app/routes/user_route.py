from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.responses import JSONResponse
from sqlalchemy.orm.exc import NoResultFound
from sqlalchemy.orm import Session
from sqlalchemy import select, update, delete, insert

from app.database.settings import get_db
from app.schemas.user_schema import UserCreate, UserShow
from app.models.user_model import User

router_user = APIRouter()


@router_user.post("/users")
def create_user(request: UserCreate, session: Session = Depends(get_db)):
    try:
        session.execute(
            insert(User).values(
                username=request.username,
                email=request.email,
                password=request.password,
            )
        )
        session.commit()
        return JSONResponse(
            status_code=status.HTTP_201_CREATED,
            content={"message": "User created successfully"},
        )

    except Exception as error:
        return HTTPException(status_code=404, detail=str(error))


@router_user.get(
    "/users/{user_id}",
    response_model=UserShow,
    status_code=status.HTTP_200_OK,
)
def get_user(user_id: int, session: Session = Depends(get_db)):
    query = session.execute(select(User).where(User.id == user_id))
    user = query.scalar_one_or_none()
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return user


@router_user.put("/users/{user_id}")
def update_user(user_id: int, request: UserCreate, session: Session = Depends(get_db)):
    try:
        user = session.execute(
            select(User).where(User.id == user_id)
        ).scalar_one_or_none()
        if user is None:
            raise HTTPException(status_code=404, detail="User not found")
        session.execute(
            update(User)
            .where(User.id == user_id)
            .values(
                username=request.username,
                email=request.email,
                password=request.password,
            )
        )
        session.commit()
    except NoResultFound:
        raise HTTPException(status_code=404, detail="User not found")
    return JSONResponse(
        status_code=status.HTTP_204_NO_CONTENT,
        content={"message": "User updated successfully"},
    )


@router_user.delete("/users/{user_id}")
def delete_user(user_id: int, session: Session = Depends(get_db)):
    try:
        user = session.execute(
            select(User).where(User.id == user_id)
        ).scalar_one_or_none()
        if user is None:
            raise HTTPException(status_code=404, detail="User not found")
        session.execute(delete(User).where(User.id == user_id))
        session.commit()

    except NoResultFound:
        raise HTTPException(status_code=404, detail="User not found")

    return JSONResponse(
        status_code=status.HTTP_204_NO_CONTENT,
        content={"message": "User deleted successfully"},
    )
