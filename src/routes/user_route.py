from fastapi import APIRouter, HTTPException, status, Depends
from services.user_service import UserService
from schemas.user_schema import UserCreate, UserUpdate, UserResponse
from typing import List

# Create router instance for user-related routes
router = APIRouter()

# Dependency injection for user service


def get_user_service():
    db_config = {
        'host': 'localhost',
        'user': 'root',
        'password': '0329782205',
        'database': 'ebook'
    }
    return UserService(db_config)


@router.post("/users", response_model=UserResponse, status_code=status.HTTP_201_CREATED)
def register_user(user: UserCreate, user_service: UserService = Depends(get_user_service)):
    result = user_service.register_user(
        user.username, user.email, user.password)
    if "error" in result:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail=result["error"])
    return UserResponse(user_id=result["user_id"], username=user.username, email=user.email, streak=0)


@router.get("/users/{user_id}", response_model=UserResponse, status_code=status.HTTP_200_OK)
def get_user(user_id: int, user_service: UserService = Depends(get_user_service)):
    user = user_service.get_user(user_id)
    if "error" in user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail=user["error"])
    # Map database field names to Pydantic model field names
    return UserResponse(
        user_id=user["UserID"],
        username=user["UserName"],
        email=user["Email"],
        streak=user["Streak"]
    )


@router.put("/users/{user_id}", response_model=UserResponse, status_code=status.HTTP_200_OK)
def update_user(user_id: int, user_update: UserUpdate, user_service: UserService = Depends(get_user_service)):
    result = user_service.update_user_info(
        user_id, user_update.username, user_update.email, user_update.password, user_update.streak)
    if "error" in result:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail=result["error"])
    updated_user = user_service.get_user(user_id)
    if "error" in updated_user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail=updated_user["error"])
    return UserResponse(
        user_id=updated_user["UserID"],
        username=updated_user["UserName"],
        email=updated_user["Email"],
        streak=updated_user["Streak"]
    )


@router.delete("/users/{user_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_user(user_id: int, user_service: UserService = Depends(get_user_service)):
    result = user_service.delete_user(user_id)
    if "error" in result:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail=result["error"])
