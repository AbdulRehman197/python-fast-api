from fastapi import FastAPI
import pandas as pd
from json import dumps,loads
app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/readfile")
def read_file():
    df = pd.read_excel("demo.xlsx", sheet_name="Sheet2")
    return df.to_json(orient="records")