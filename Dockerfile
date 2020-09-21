FROM python:3.8.5-slim


WORKDIR /lotto

COPY webpython_hw02/* /lotto/

CMD ["python", "lotto.py"]
