from fastapi import APIRouter, HTTPException, status, Depends
from services.membership_service import MembershipService
from schemas.membership_schemas import MembershipCreate, MembershipResponse, MembershipUpdate

router = APIRouter()


def get_membership_service():
    db_config = {
        'host': 'localhost',
        'user': 'root',
        'password': '0329782205',
        'database': 'ebook'
    }
    return MembershipService(db_config)


@router.get("/memberships/{user_id}", response_model=MembershipResponse, status_code=status.HTTP_201_CREATED)
def get_membership(user_id: int, membership_service: MembershipService = Depends(get_membership_service)):
    membership = membership_service.get_membership(user_id=user_id)
    if "error" in membership:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail=membership["error"])
    return MembershipResponse(
        user_id=user_id,
        type=membership["Type"],
        expired_day=membership["ExpiredDay"],
        remaining_books=membership["RemainingBooks"]
    )


@router.put("/membership/{user_id}", response_model=MembershipResponse, status_code=status.HTTP_200_OK)
def update_membership(user_id: int, membership_update: MembershipUpdate, membership_service: MembershipService = Depends(get_membership_service)):
    result = membership_service.update_membership_info(
        user_id=user_id,
        type=membership_update.type,
        expired_day=membership_update.expired_day,
        remaining_books=membership_update.remaining_books)

    if "error" in result:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail=result["error"])
    updated_membership = membership_service.get_membership(user_id=user_id)
    if "error" in updated_membership:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail=updated_membership["error"])
    return MembershipResponse(
        user_id=user_id,
        type=updated_membership["Type"],
        expired_day=updated_membership["ExpiredDay"],
        remaining_books=updated_membership["RemainingBooks"]
    )


@router.post("/membership/{user_id}", response_model=MembershipResponse, status_code=status.HTTP_200_OK)
def create_membership(user_id: int, membership: MembershipCreate, membership_service: MembershipService = Depends(get_membership_service)):
    result = membership_service.create_membership(user_id=user_id,
                                                  type=membership.type,
                                                  expired_day=membership.expired_day,
                                                  remaining_books=membership.remaining_books)
    print(result)
    if "error" in result:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail=result["error"])
    return MembershipResponse(
        user_id=user_id,
        type=membership.type,
        expired_day=membership.expired_day,
        remaining_books=membership.remaining_books
    )


@router.delete("/membership/{user_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_membership_by_user_id(user_id: int, membership_service: MembershipService = Depends(get_membership_service)):
    result = membership_service.delete_membership(user_id=user_id)
    if "error" in result:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail=result["error"])
