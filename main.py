from fastapi import FastAPI

app = FastAPI(
    title="Trading App"
)


fake_users = [
    {"id": 1, "role": "admin", "name": "Bob"},
    {"id": 2, "role": "investor", "name": "Max"},
    {"id": 3, "role": "traider", "name": "Stas"},
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


@app.get("/users/{user_id}")
def get_data_for_user(user_id: int):
    user = list(filter(lambda x: x.get("id") == int(user_id), fake_users))
    if not user:
        return {}
    return user[0]


@app.get("/trades")
def get_trades(limit: int = 1, offset: int = 1):
    return fake_trades[offset:][:limit]


@app.post("/users/{user_id}")
def change_user_name(user_id: int, new_name: str):
    user = list(filter(lambda x: x.get("id") == int(user_id), fake_extra_users))
    if not user:
        return {"status": 404, "data": "Have no that user"}

    user = user[0]
    user["name"] = new_name
    return {"status": 200, "operation_result": user}
