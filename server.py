from fastapi import FastAPI

app = FastAPI()

@app.get("/leads")
def get_leads():
    return [{"id": 1, "name": "Ramesh Singh", "status": "Converted"}]

@app.get("/lead/{id}")
def get_lead(id: int):
    return {"id": id, "name": "Ramesh Singh", "contact": "9876543210", "status": "Contacted"}

@app.get("/users")
def get_users():
    return [{"id": 1, "name": "Executive A"}, {"id": 2, "name": "Admin B"}]

added server.py
