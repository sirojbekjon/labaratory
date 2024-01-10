FROM python:3.8-alpine

WORKDIR /app

COPY reqs.txt .

RUN pip install -r reqs.txt

COPY . .

CMD ["python3", "-m" , "flask", "run", "--host=0.0.0.0"]
