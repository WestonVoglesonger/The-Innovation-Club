"""Productivity API

Productivity routes are used to create, retrieve, and update Pomodoro timers."""

from fastapi import APIRouter, Depends

from backend.models.admin_data import AdminData
from backend.models.admin_create_data import AdminCreate

from backend.services.exceptions import AdminRegistrationException
from ..services.admin import AdminService


api = APIRouter(prefix="/api/admin")
openapi_tags = {
    "name": "Admin",
    "description": "Create, update, delete, and retrieve admin data.",
}


# GET /api/admin
# Gets all admins.
# Expected return type: list[AdminData]
@api.get("", response_model=list[AdminData], tags=["Admin"])
def get_admins(
    admin_service: AdminService = Depends(),
) -> list[AdminData]:
    """
    Get all admins.

    Parameters:
        admin_service: a valid AdminService

    Returns:
        list[AdminData]: All admins
    """

    # Return all admins
    return admin_service.get_admins()


# GET /api/admin/{id}
# Get a admin by its ID.
# Expected return type: AdminData
@api.get("/{id}", response_model=AdminData, tags=["Admin"])
def get_admin(
    id: int,
    admin_service: AdminService = Depends(),
) -> AdminData:
    """
    Get admin.

    Parameters:
        id: ID of the admin to get
        admin_service: a valid AdminService
    """

    return admin_service.get_admin(id)


# POST /api/admin/
# Creates a new admin.
# Expected return type: AdminData
@api.post("", response_model=AdminData, tags=["Admin"])
def create_admin(
    admin_create: AdminCreate,
    admin_service: AdminService = Depends(),
) -> AdminData:
    """
    Create admin.

    Parameters:
        admin: a valid admin model
        admin_service: a valid AdminService

    Returns:
        admin: Created admin
    """

    return admin_service.create_admin(admin_create)


# PUT /api/admin
# Updates a admin.
# Expected return type: AdminData
@api.put("", response_model=AdminData, tags=["Admin"])
def update_admin(
    admin: AdminData,
    admin_service: AdminService = Depends(),
) -> AdminData:
    """
    Update admin.

    Parameters:
        admin: a valid AdminData model
        admin_service: a valid AdminService

    Returns:
        AdminData: Updated admin
    """

    return admin_service.update_admin(admin)


# DELETE /api/admin/{id}
# Deletes a admin.
# Expected return type: AdminData
@api.delete("/{id}", response_model=None, tags=["Admin"])
def delete_admin(
    id: int,
    admin_service: AdminService = Depends(),
) -> AdminData:
    """
    Delete admin.

    Parameters:
        id: ID of the admin to delete
        admin_service: a valid AdminService
    """

    return admin_service.delete_admin(id) # type: ignore

@api.get("/check-email/{email}", response_model=bool)
def check_email_registered(email: str, admin_service: AdminService = Depends()) -> bool:
    """
    Check if an email is already registered.

    Parameters:
        email: Email to check

    Returns:
        bool: True if email is registered, False otherwise
    """
    return admin_service.check_email_registered(email)