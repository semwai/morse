# no need to use pipenv in production server, get list of packages in builder and install them via pip
FROM python:3.10 as builder

RUN pip install pipenv

WORKDIR /app

COPY Pipfile* .

COPY . .

RUN pipenv requirements > requirements.txt

FROM python:3.10-alpine

WORKDIR /app

COPY --from=builder /app /app

RUN pip install -r requirements.txt

EXPOSE 8000

ENTRYPOINT ["python", "src/app.py"]