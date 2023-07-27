from datetime import datetime

from sqlalchemy import (
    MetaData, Column, Table, Integer, String, TIMESTAMP, ForeignKey, JSON
)

metadata = MetaData()

roles = Table(
    "roles",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("name", String, nullable=False),
    Column("permissions", JSON),
)

users = Table(
    "users",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("email", String, nullable=False),
    Column("name", String, nullable=False),
    Column("password", String, nullable=False),
    Column("registered_at", TIMESTAMP, default=datetime.now),
    Column("role_id", Integer, ForeignKey("roles.id")),
)