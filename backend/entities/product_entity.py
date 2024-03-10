from sqlalchemy import Column, Integer, String, UniqueConstraint
from sqlalchemy.orm import Mapped, mapped_column
from typing import Self

from backend.models.product_data import ProductData
from .entity_base import EntityBase

__authors__ = ["Weston Voglesonger"]
__copyright__ = "Copyright 2023"
__license__ = "MIT"


class ProductEntity(EntityBase):
    """Serves as the database model schema defining the shape of the `Product` table"""

    __tablename__ = "product"
    __table_args__ = (
        UniqueConstraint('url'),
    )

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String(50), nullable=False)
    description: Mapped[str] = mapped_column(String(100), nullable=False)
    url: Mapped[str] = mapped_column(String(2083), nullable=False, unique=True)

    @classmethod
    def from_model(cls, model: ProductData) -> Self:
        """
        Create a ProductEntity from a ProductData model.

        Args:
            model (ProductData): The model to create the entity from.

        Returns:
            Self: The entity (not yet persisted).
        """
        return cls(
            id=model.id,
            name=model.name,
            description=model.description,
            url=model.url,
        )

    def to_model(self) -> ProductData:
        """
        Create a ProductData model from a ProductEntity.

        Returns:
            ProductData: A ProductData model for API usage.
        """
        return ProductData(
            id=self.id,
            name=self.name,
            description=self.description,
            url=self.url,
        )
