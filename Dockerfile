FROM python:latest

COPY . .

ENTRYPOINT ["python", "jogos.py"]
