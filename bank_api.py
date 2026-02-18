from fastapi import FastAPI
from pydantic import BaseModel

class Account(BaseModel):
    id: int
    name: str
    sold: float
    status: str

accounts = []

app = FastAPI()

@app.post("/accounts")
def create_account(account : Account):
    accounts.append(account)
    return "le compte à bine été créé"

@app.get("/accounts")
def get_accounts():
    return accounts