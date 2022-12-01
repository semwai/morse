from fastapi import FastAPI
from fastapi.responses import PlainTextResponse, JSONResponse
from fastapi.exceptions import HTTPException
import uvicorn

from morse import encode, decode
from alphabets import table

app = FastAPI()


@app.get('/encode')
def index(text: str, lang: str = 'en'):
    try:
        res = encode(text, table(lang))
        return PlainTextResponse(res)
    except NotImplementedError as e:
        raise HTTPException(400, str(e))


@app.get('/decode')
def index(text: str, lang: str = 'en'):
    try:
        res = decode(text, table(lang))
        return PlainTextResponse(res)
    except NotImplementedError as e:
        raise HTTPException(400, str(e))


@app.get('/alphabet')
def index(lang: str = 'en'):
    try:
        res = table(lang)
        return JSONResponse(res)
    except NotImplementedError as e:
        raise HTTPException(400, str(e))


if __name__ == '__main__':
    uvicorn.run('app:app', host='0.0.0.0', port=8000, reload=True)
