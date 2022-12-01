from fastapi import FastAPI
from fastapi.exceptions import HTTPException
import uvicorn

from morse import encode, decode
from alphabets import table
from models import TextResponse, AlphabetResponse

app = FastAPI()


@app.get('/encode', response_model=TextResponse)
def get_encode(text: str, lang: str = 'en'):
    try:
        res = encode(text, table(lang))
        return TextResponse(data=res)
    except NotImplementedError as e:
        raise HTTPException(400, str(e))


@app.get('/decode', response_model=TextResponse)
def get_decode(text: str, lang: str = 'en'):
    try:
        res = decode(text, table(lang))
        return TextResponse(data=res)
    except NotImplementedError as e:
        raise HTTPException(400, str(e))


@app.get('/alphabet', response_model=AlphabetResponse)
def get_alphabet(lang: str = 'en'):
    try:
        res = table(lang)
        return AlphabetResponse(data=res)
    except NotImplementedError as e:
        raise HTTPException(400, str(e))


if __name__ == '__main__':
    uvicorn.run('app:app', host='0.0.0.0', port=8000, reload=True)
