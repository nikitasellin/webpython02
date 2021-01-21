FROM python:3.8.5-slim


WORKDIR /app

COPY app/requirements.txt /app/
RUN pip install -r requirements.txt

COPY app/ /app/

CMD ["python", "lotto.py"]
