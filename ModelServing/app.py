from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class InputData(BaseModel):
    value: int

@app.post("/model2")
async def model2(data: InputData):
    # Простая модель, добавляющая 10
    result = {'result': data.value + 10}
    return result