from fastapi import FastAPI
from pydantic import BaseModel
import httpx

app = FastAPI()

class InputData(BaseModel):
    value: int

@app.post("/process")
async def process(data: InputData):
    async with httpx.AsyncClient() as client:
        # Вызов feature_extraction
        response_feature_extraction = await client.post('http://feature_extraction:5001/model1', json=data.dict())
        result_feature_extraction = response_feature_extraction.json()

        # Вызов model_serving
        response_model_serving = await client.post('http://model_serving:5002/model2', json=data.dict())
        result_model_serving = response_model_serving.json()

    # Обработка результатов и возврат финального ответа
    final_result = {
        'model1_output': result_feature_extraction,
        'model2_output': result_model_serving,
        'final_result': result_feature_extraction['result'] + result_model_serving['result']
    }
    return final_result