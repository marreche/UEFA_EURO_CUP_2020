FROM python:3.9.7

ADD ./ /Euro2020api

WORKDIR /Euro2020api

RUN pip install -r requirements.txt

CMD ["python","Euro_cup_2020_api/main.py"]