from datetime import datetime
from enum import Enum
from typing import List, Optional

from fastapi import FastAPI

#  uvicorn main:app --reload
from pydantic import BaseModel

app = FastAPI(
    title="Trading App"
)


fake_users = [
    {"id": 1, "role": "admin", "name": "Bob"},
    {"id": 2, "role": "investor", "name": "Max"},
    {"id": 3, "role": "traider", "name": "Stas"},
    {"id": 4, "role": "investor", "name": "Stas", "degree": [
        {"id": 1, "created_at": "2020-01-01T00:00:00", "type_degree": "expert"}
    ]},
]

fake_extra_users = [
    {"id": 1, "role": "admin", "name": "Bob"},
    {"id": 2, "role": "investor", "name": "Max"},
    {"id": 3, "role": "traider", "name": "Stas"},
]

fake_trades = [
    {"id": 1, "user_id": 1, "currency": "BTC", "side": "buy", "price": 123, "amount": 2.12},
    {"id": 2, "user_id": 2, "currency": "ETH", "side": "sell", "price": 100, "amount": 515},
]


class Trade(BaseModel):
    id: int
    user_id: int
    currency: str
    side: str
    price: int
    amount: float


class DegreeType(Enum):
    newbie = "newbie"
    expert = "expert"


class Degree(BaseModel):
    id: int
    created_at: datetime
    type_degree: DegreeType


class User(BaseModel):
    id: int
    role: str
    name: str
    degree: Optional[List[Degree]] = []


@app.get("/users/{user_id}", response_model=List[User])
def get_data_for_user(user_id: int):
    return [user for user in fake_users if user.get("id") == int(user_id)]


@app.post("/users/{user_id}")
def change_user_name(user_id: int, new_name: str):
    user = list(filter(lambda x: x.get("id") == int(user_id), fake_extra_users))
    if not user:
        return {"status": 404, "data": "Have no that user"}

    user = user[0]
    user["name"] = new_name
    return {"status": 200, "operation_result": user}


@app.post("/trades")
def add_trades(trades: List[Trade]):
    fake_trades.extend(trades)
    return {"status": 200, "data": fake_trades}

