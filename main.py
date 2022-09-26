import uvicorn
from fastapi import FastAPI

print("Hello fastapi")
api = FastAPI()


# Decorator:
@api.get('/')
def endpoint():
    return {"msg": "Hello everyone",
            "another msg": ["Hello", "Keys"]}


uvicorn.run(api, port=9966)
