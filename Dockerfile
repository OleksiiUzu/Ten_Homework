FROM python:latest
COPY . .
WORKDIR .

EXPOSE 5001
RUN pip install -r requirements.txt

CMD ["python", "app.py"]