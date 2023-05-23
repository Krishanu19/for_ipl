FROM python:3.8-slim

WORKDIR for_ipl

COPY ./requirements.txt .

RUN pip install -r requirements.txt

COPY . .

EXPOSE 8080

CMD python -m uvicorn main:app --reload --host 0.0.0.0 --port 8000