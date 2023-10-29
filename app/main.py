from fastapi import FastAPI
from sqlalchemy import create_engine

DATABASE_URL = "postgresql://user:password@db/mydatabase"

engine = create_engine(DATABASE_URL)

app = FastAPI()

@app.get("/")
def read_root():
    # ここでデータベースを使用するコードを追加できます
    return {"Hello": "World"}
