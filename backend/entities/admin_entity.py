"""Definition of SQLAlchemy table-backed object mapping entity for Admin."""
from sqlalchemy import Column, Integer, String, UniqueConstraint
from sqlalchemy.orm import Mapped, mapped_column, relationship
from typing import Self

from  backend.models.admin_data import AdminData
from  backend.models.admin_data import AdminData
from .entity_base import EntityBase

__authors__ = ["Weston Voglesonger"]
__copyright__ = "Copyright 2023"
__license__ = "MIT"


class AdminEntity(EntityBase):
    """Serves as the database model schema defining the shape of the `AdminData` table"""

    __tablename__ = "admin"
    __tablename__ = "admin"
    __table_args__ = (
        UniqueConstraint('email'),
    )

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    first_name: Mapped[str] = mapped_column(String(50), nullable=False)
    last_name: Mapped[str] = mapped_column(String(50), nullable=False)
    email: Mapped[str] = mapped_column(String(100), nullable=False, unique=True)
    hashed_password: Mapped[str] = mapped_column(String(100), nullable=False)

    # Example relationship (if applicable)
    # posts = relationship("PostEntity", back_populates="admin")

    @classmethod
    def from_model(cls, model: AdminData) -> Self:
        """
        Create a AdminEntity from a AdminData model.

        Args:
            model (AdminData): The model to create the entity from.
            model (AdminData): The model to create the entity from.

        Returns:
            Self: The entity (not yet persisted).
        """
        return cls(
            id=model.id,
            first_name=model.first_name,
            last_name=model.last_name,
            hashed_password=model.hashed_password,
            email=model.email,
        )

    def to_model(self) -> AdminData:
        """
        Create a AdminData model from a AdminEntity.

        Returns:
            Admin: A AdminData model for API usage.
        """
        return AdminData(
            id=self.id,
            first_name=self.first_name,
            last_name=self.last_name,
            email=self.email,
            hashed_password=self.hashed_password,
        )