from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class InputData(BaseModel):
    value: int

@app.post("/model1")
async def model1(data: InputData):
    # Простая модель, умножающая на 2
    result = {'result': data.value * 2}
    return result