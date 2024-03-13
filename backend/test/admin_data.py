"""Mock data for admins.

Three admins are setup for testing and development purposes:

1. Rhonda Root (root admin with all permissions)
2. Amy Ambassador (staff of XL with elevated permissions)
3. Sally Student (standard admin without any special permissions)"""

import pytest
from sqlalchemy.orm import Session
from backend.entities.admin_entity import AdminEntity

from backend.models.admin_data import AdminData
from backend.test.services.reset_table_id_seq import reset_table_id_seq

__authors__ = ["Kris Jordan", "Weston Voglesonger"]
__copyright__ = "Copyright 2023"
__license__ = "MIT"

root = AdminData(
    id=1,
    first_name="root",
    last_name="root",
    email="root@unc.edu",
    hashed_password="password",
)

updated_root = AdminData(
    id=1,
    first_name="updated",
    last_name="updated",
    email="root@unc.edu",
    hashed_password="updated-password",
)

admin = AdminData(
    id=2,
    first_name="admin",
    last_name="admin",
    email="admin@unc.edu",
    hashed_password="password",
)
admins = [root]


def insert_fake_data(session: Session):
    global admins
    entities = []
    for admin in admins:
        entity = AdminEntity.from_model(admin)
        session.add(entity)
        entities.append(entity)
    reset_table_id_seq(session, AdminEntity, AdminEntity.id, len(admins) + 1)
    session.commit()  # Commit to ensure admin IDs in database


@pytest.fixture(autouse=True)
def fake_data_fixture(session: Session):
    insert_fake_data(session)
    session.commit()
    yield
