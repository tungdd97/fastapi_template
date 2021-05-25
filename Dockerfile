FROM python:3.8

RUN pip install -r requirements.txt

EXPOSE 8080

COPY ./fastapi_template /fastapi_template

CMD ["uvicorn", "start_app:app", "--host", "0.0.0.0", "--port", "8080"]