import pytest
from ...services.product import ProductService
from ...entities.product_entity import ProductEntity
from ...models.product_data import ProductData
from ...services.exceptions import (
    ResourceNotFoundException,
    ProductRegistrationException,
)
from .fixtures import product_service
from ..product_data import fake_data_fixture, product_1, new_product, updated_product

from ...models.product_data import ProductData

def test_get_products(product_service: ProductService) -> None:
    products = product_service.get_products()
    assert len(products) == 1 
    
def test_get_product(product_service: ProductService) -> None:
    product = product_service.get_product(product_1.id)
    assert product.id == product_1.id
    assert product.name == product_1.name
    assert product.description == product_1.description
    assert product.url == product_1.url

def test_get_product_non_existent(product_service: ProductService) -> None:
    with pytest.raises(ResourceNotFoundException):
        product_service.get_product(999)

def test_create_product(product_service: ProductService) -> None:
    updated_product = ProductData(
    id=None,
    name="Updated Product",
    description="This product has been updated",
    url="https://github.com/example/updated-product"
    )

    created_product = product_service.create_product(updated_product)
    assert created_product is not None
    assert created_product.name == updated_product.name
    assert created_product.description == updated_product.description
    assert created_product.url == updated_product.url

def test_create_product_existing_name(product_service: ProductService) -> None:
    with pytest.raises(ProductRegistrationException):
        product_service.create_product(product_1)

def test_update_product(product_service: ProductService) -> None:
    new_updated_product = product_service.update_product(updated_product)
    assert new_updated_product.name == updated_product.name
    assert new_updated_product.description == updated_product.description
    assert new_updated_product.url == updated_product.url

def test_update_product_non_existent(product_service: ProductService) -> None:
    with pytest.raises(ResourceNotFoundException):
        product_service.update_product(new_product)

def test_delete_product(product_service: ProductService) -> None:
    product_service.delete_product(product_1.id)
    with pytest.raises(ResourceNotFoundException):
        product_service.get_product(product_1.id)

def test_delete_product_non_existent(product_service: ProductService) -> None:
    with pytest.raises(ResourceNotFoundException):
        product_service.delete_product(999)

