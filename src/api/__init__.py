from functools import wraps

from fastapi import FastAPI
from fastapi.responses import JSONResponse

app = FastAPI()


def build_message_susccess(message):
    return {"message": message, "code": 200}


def try_except_response(func):
    @wraps(func)
    async def wrapper(*args, **kwargs):
        try:
            return JSONResponse(status_code=200, content=func(*args, **kwargs))
        except:
            return JSONResponse(status_code=404, content=func(*args, **kwargs))

    return wrapper
