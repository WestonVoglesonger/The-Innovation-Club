import pytest
from ...services.admin import AdminService
from ...entities.admin_entity import AdminEntity
from ...models.admin_data import AdminData
from ...services.exceptions import (
    ResourceNotFoundException,
    AdminRegistrationException,
)
from .fixtures import admin_service
from ..admin_data import fake_data_fixture, updated_root, admin


def test_get_admins(admin_service: AdminService) -> None:
    admins = admin_service.get_admins()
    assert len(admins) == 1 
    
def test_get_admin(admin_service: AdminService) -> None:
    admin_id = 1
    admin = admin_service.get_admin(admin_id)
    assert admin.id == admin_id
    assert admin.first_name == "root"
    assert admin.last_name == "root"
    assert admin.email == "root@unc.edu"

def test_create_admin(admin_service: AdminService) -> None:
    created_admin = admin_service.create_admin(admin)
    assert created_admin.email == admin.email

def test_create_admin_existing_email(admin_service: AdminService) -> None:
    with pytest.raises(AdminRegistrationException):
        admin_service.create_admin(updated_root)

def test_update_admin(admin_service: AdminService) -> None:
    updated_admin = admin_service.update_admin(updated_root)
    assert updated_admin.first_name == "updated"
    assert updated_admin.last_name == "updated"

def test_update_admin_non_existent(admin_service: AdminService) -> None:
    with pytest.raises(ResourceNotFoundException):
        admin_service.update_admin(admin)

def test_delete_admin(admin_service: AdminService) -> None:
    admin_service.delete_admin(1)
    with pytest.raises(ResourceNotFoundException):
        admin_service.get_admin(1)

def test_delete_admin_non_existent(admin_service: AdminService) -> None:
    with pytest.raises(ResourceNotFoundException):
        admin_service.delete_admin(999)

def test_get_admin_by_id_not_found(admin_service: AdminService) -> None:
    with pytest.raises(ResourceNotFoundException):
        admin_service.get_admin(999)

def test_check_email_registered(admin_service: AdminService) -> None:
    assert admin_service.check_email_registered("root@unc.edu") is True
    assert admin_service.check_email_registered("nonexistent@example.com") is False
