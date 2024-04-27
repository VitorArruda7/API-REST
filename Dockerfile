FROM python:latest

WORKDIR /api

COPY main.py ./
COPY atendimentos.csv ./

RUN pip install flask


EXPOSE 8001


CMD ["python", "main.py"]