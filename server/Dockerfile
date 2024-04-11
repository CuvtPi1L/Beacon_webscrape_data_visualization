FROM python:3.10-alpine

COPY requirement.txt /app/

COPY src /app/

WORKDIR /app

ENV FLASK_APP=app.py
ENV FLASK_RUN_HOST=0.0.0.0

RUN pip install -r requirement.txt

# RUN python createTable.py

RUN python dataSeed.py

CMD ["flask","run"]