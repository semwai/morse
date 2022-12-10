# Morse code v1.1.0

## service for converting morse code to text and vice versa

## Run tests
```bash
pipenv shell
pipenv install 
pytest
```

## Run server: 

```bash
docker build -t morse . 
docker run -it --rm -p 88:8000 morse
```
## open [localhost:88](localhost:88]) in your browser or use curl

```curl
curl -X 'GET' \
  'http://localhost:88/decode?text=...%20---%20...&lang=en' \
  -H 'accept: application/json'
```

```json
{
  "data": "SOS"
}
```


```bash
curl -X 'GET' \
  'http://localhost:88/alphabet?lang=ru' \
  -H 'accept: application/json'
```

```json
{
  "data": {
    "0": "-----",
    "1": ".----",
    "2": "..---",
    "3": "...--",
    "4": "....-",
    "5": ".....",
    "6": "-....",
    "7": "--...",
    "8": "---..",
    "9": "----.",
    "А": ".-",
    "Б": "-...",
    "В": ".--",
    "Г": "--.",
    "Д": "-..",
    "Е": ".",
    "Ж": "...-",
    "З": "--..",
    "И": "..",
    "Й": ".---",
    "К": "-.-",
    "Л": ".-..",
    "М": "--",
    "Н": "-.",
    "О": "---",
    "П": ".--.",
    "Р": ".-.",
    "С": "...",
    "Т": "-",
    "У": "..-",
    "Ф": "..-.",
    "Х": "....",
    "Ц": "-.-.",
    "Ч": "---.",
    "Ш": "----",
    "Щ": "--.-",
    "Ъ": ".--.-.",
    "Ы": "-.--",
    "Ь": "-..-",
    "Э": "...-...",
    "Ю": "..--",
    "Я": ".-.-",
    ", ": "--..--",
    ".": ".-.-.-",
    "?": "..--..",
    "/": "-..-.",
    "-": "-....-",
    "(": "-.--.",
    ")": "-.--.-"
  }
}
```

## open [localhost:88/docs](localhost:88/docs]) in your browser for swagger UI interactive documentation

## Changelog 1.0.0 -> 1.1.0
- add tests
- fix encode bug