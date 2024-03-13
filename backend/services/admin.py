from fastapi import Depends
from sqlalchemy.orm import Session
from ..database import db_session
from ..entities.admin_entity import AdminEntity
from ..models.admin_data import AdminData
from .exceptions import (
    ResourceNotFoundException,
    AdminRegistrationException,
)

import os
from dotenv import load_dotenv

load_dotenv()

ACCESS_CODE = os.getenv("ACCESS_CODE")


from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


class AdminService:
    """Backend service that enables direct modification of admin data."""

    def __init__(self, session: Session = Depends(db_session)):
        """Initializes the 'AdminService` session"""
        self._session = session

    def get_admins(self) -> list[AdminData]:
        """Retrieves all admins."""
        query_result = self._session.query(AdminEntity).all()
        return [admin_entity.to_model() for admin_entity in query_result]

    def get_admin(self, admin_id: int) -> AdminData:
        """Gets one admin by an ID."""
        admin_entity = (
            self._session.query(AdminEntity).filter(AdminEntity.id == admin_id).first()
        )
        if admin_entity is None:
            raise ResourceNotFoundException("admin does not exist.")
        return admin_entity.to_model()

    def create_admin(self, admin: AdminData) -> AdminData:
        """Stores an admin in the database."""
        existing_email = (
            self._session.query(AdminEntity)
            .filter(AdminEntity.email == admin.email)
            .first()
        )
        if existing_email:
            raise AdminRegistrationException()

        # Hash the password before storing it
        hashed_password = pwd_context.hash(admin.hashed_password)
        admin.hashed_password = hashed_password

        new_admin = AdminEntity.from_model(admin)
        self._session.add(new_admin)
        self._session.commit()
        return new_admin.to_model()

    def update_admin(self, admin: AdminData) -> AdminData:
        """Modifies one admin in the database."""
        admin_entity = (
            self._session.query(AdminEntity).filter(AdminEntity.id == admin.id).first()
        )
        if admin_entity is None:
            raise ResourceNotFoundException("admin does not exist.")

        admin_entity.first_name = admin.first_name
        admin_entity.last_name = admin.last_name
        admin_entity.email = admin.email
        self._session.commit()
        return admin_entity.to_model()

    def delete_admin(self, admin_id: int) -> None:
        """Deletes one admin from the database."""
        admin_entity = (
            self._session.query(AdminEntity).filter(AdminEntity.id == admin_id).first()
        )
        if admin_entity is None:
            raise ResourceNotFoundException("admin does not exist.")

        self._session.delete(admin_entity)
        self._session.commit()

    def check_email_registered(self, email: str) -> bool:
        """Checks if an email is already registered."""
        existing_email = (
            self._session.query(AdminEntity).filter(AdminEntity.email == email).first()
        )
        return existing_email is not None

    def update_admin_password(self, admin_id: int, new_password: str) -> None:
        """Updates the password of an admin in the database."""
        admin_entity = (
            self._session.query(AdminEntity).filter(AdminEntity.id == admin_id).first()
        )
        if admin_entity is None:
            raise ResourceNotFoundException("Admin does not exist.")

        hashed_password = pwd_context.hash(new_password)
        admin_entity.hashed_password = hashed_password
        self._session.commit()

    def verify_admin_password(self, email: str, password: str) -> bool:
        """Verifies the password of an admin."""
        admin_entity = (
            self._session.query(AdminEntity).filter(AdminEntity.email == email).first()
        )
        if admin_entity is None:
            return False

        return pwd_context.verify(password, admin_entity.hashed_password)

    def verify_access_code(self, access_code: str) -> bool:
        """Verifies the access code."""
        return access_code == ACCESS_CODE
