"""Productivity API

Productivity routes are used to create, retrieve, and update Pomodoro timers."""

from fastapi import APIRouter, Depends

from backend.models.product_data import ProductData
from backend.services.exceptions import ProductRegistrationException
from ..services.product import ProductService


api = APIRouter(prefix="/api/product")
openapi_tags = {
    "name": "Product",
    "description": "Create, update, delete, and retrieve product data.",
}


# GET /api/join
# Gets all users.
# Expected return type: list[ProductData]
@api.get("", response_model=list[ProductData], tags=["Product"])
def get_products(
    product_service: ProductService = Depends(),
) -> list[ProductData]:
    """
    Get all products.

    Parameters:
        product_service: a valid ProductService

    Returns:
        list[ProductData]: All products
    """

    # Return all users
    return product_service.get_products()


# GET /api/product/{id}
# Get a product by its ID.
# Expected return type: ProductData
@api.get("/{id}", response_model=ProductData, tags=["Product"])
def get_product(
    id: int,
    product_service: ProductService = Depends(),
) -> ProductData:
    """
    Get product.

    Parameters:
        id: ID of the product to get
        product_service: a valid ProductService
    """

    return product_service.get_product(id)


# POST /api/product/
# Creates a new product.
# Expected return type: ProductData
@api.post("", response_model=ProductData, tags=["Product"])
def create_product(
    product: ProductData,
    product_service: ProductService = Depends(),
) -> ProductData:
    """
    Create product.

    Parameters:
        product: a valid product model
        product_service: a valid ProductService

    Returns:
        User: Created product
    """
    return product_service.create_product(product)


# PUT /api/product
# Updates a product.
# Expected return type: ProductData
@api.put("", response_model=ProductData, tags=["Product"])
def update_product(
    product: ProductData,
    product_service: ProductService = Depends(),
) -> ProductData:
    """
    Update product.

    Parameters:
        product: a valid ProductData model
        product_service: a valid ProductService

    Returns:
        ProductData: Updated product
    """

    return product_service.update_product(product)


# DELETE /api/product/{id}
# Deletes a product.
# Expected return type: ProductData
@api.delete("/{id}", response_model=None, tags=["Product"])
def delete_product(
    id: int,
    product_service: ProductService = Depends(),
) -> ProductData:
    """
    Delete product.

    Parameters:
        id: ID of the product to delete
        product_service: a valid ProductService
    """

    return product_service.delete_product(id)