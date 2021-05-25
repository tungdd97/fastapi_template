FROM python:3.8

COPY ./	/

RUN pip install -r requirement.txt

EXPOSE 8080

CMD ["uvicorn", "start_app:app", "--host", "0.0.0.0", "--port", "8080"]
