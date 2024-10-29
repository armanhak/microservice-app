## Tech Stack

- 🐍 **Languages**: Python
- 🚀 **Frameworks**: FastAPI
- 🛠 **Tools**: Docker

## Запуск системы

Перейдите в корневую папку проекта и выполните команду:
```sh
docker-compose -f "docker-compose.yml" up --build
```

## Тестирование

Отправьте POST-запрос на основной сервис (Inference):
```sh
curl -X POST http://localhost:5000/process -H "Content-Type: application/json" -d '{"value": 5}'
```

Ожидаемый ответ:
```json
{
  "model1_output": {
    "_comment": "input_value * 2",
    "result": 10
  },
  "model2_output": {
    "_comment": "input_value + 10",

    "result": 15
  },
    "_comment": "model1_output + model2_output",

  "final_result": 25
}
```
